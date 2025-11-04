import marimo

__generated_with = "0.16.5"
app = marimo.App()


@app.cell
def _():
    import os
    import requests
    from dotenv import load_dotenv
    import google.generativeai as genai
    return genai, load_dotenv, os, requests


@app.cell
def _():
    import marimo as _mo

    url_input = _mo.ui.text(
        label="URL", placeholder="https://example.com", value="")
    run_btn = _mo.ui.run_button(label="Scrape & summarize")
    _mo.hstack([url_input, run_btn])
    return run_btn, url_input


@app.cell
def _(load_dotenv, os, requests):
    import marimo as _mo
    from pathlib import Path
    load_dotenv()

    try:
        load_dotenv(dotenv_path=Path(
            __file__).with_name(".env"), override=False)
    except Exception:
        pass
    steel_key = os.getenv("STEEL_API_KEY")
    google_key = os.getenv("GEMINI_API_KEY")

    def steel_fetch_text(url: str, api_key: str) -> str:
        if not api_key:
            return "ERROR: STEEL_API_KEY nije postavljen (.env)."
        try:
            import json
            from bs4 import BeautifulSoup

            resp = requests.post(
                "https://api.steel.dev/v1/scrape",
                headers={
                    "steel-api-key": api_key,
                    "content-type": "application/json",
                    "accept": "application/json",
                },
                json={
                    "url": url,
                    "extract": "text",
                    "useProxy": False,
                    "delay": 1,
                    "fullPage": True,
                    "region": "",
                },
            )
            ct = resp.headers.get("content-type", "")
            if "application/json" in ct:
                data = resp.json()
                if isinstance(data, dict):
                    for key in ("text", "content", "extracted_text"):
                        val = data.get(key)
                        if isinstance(val, str) and val.strip():
                            return val
                    content = data.get("content")
                    if isinstance(content, dict):
                        html = content.get("html") or content.get("body")
                        if isinstance(html, str) and html.strip():
                            soup = BeautifulSoup(html, "html.parser")
                            return soup.get_text(" ", strip=True)
                    html = data.get("html")
                    if isinstance(html, str) and html.strip():
                        soup = BeautifulSoup(html, "html.parser")
                        return soup.get_text(" ", strip=True)
                    return json.dumps(data, ensure_ascii=False)
                if isinstance(data, list):
                    return "\n".join(str(item) for item in data)
                return str(data)
            return resp.text
        except Exception as e:
            return f"ERROR contacting Steel: {e}"

    return google_key, steel_fetch_text, steel_key


@app.cell
def _(genai):
    def gemini_summarize(excerpt: str, api_key: str) -> str:
        if not api_key:
            return "ERROR: GOOGLE_API_KEY nije postavljen (.env)."
        try:
            genai.configure(api_key=api_key)
            # Dynamically find a model that supports generateContent
            try:
                models = list(genai.list_models())
            except Exception:
                models = []
            candidate_models = []
            for m in models:
                try:
                    methods = getattr(
                        m, "supported_generation_methods", []) or []
                    if "generateContent" in methods:
                        candidate_models.append(getattr(m, "name", ""))
                except Exception:
                    continue
            # Ensure some reasonable defaults at the end
            candidate_models += [
                "gemini-1.5-flash-latest",
                "gemini-1.5-flash",
                "gemini-1.5-pro-latest",
            ]
            prompt = (
                "Analziraj rezultate webscrapinga. Vrati najvažnije informacije i izradi plan koraka koji bi korisnik mogao koristiti kao podsjetnik tijekom učenja sadržaja sa ove stranice.\n\n"
                "Isječak:\n" + excerpt
            )
            last_err = None
            for model_name in candidate_models:
                try:
                    if not model_name:
                        continue
                    model = genai.GenerativeModel(model_name)
                    resp = model.generate_content(prompt)
                    text = getattr(resp, "text", "") or "(prazan odgovor)"
                    # If model still returned JSON, try to prettify to human bullets
                    try:
                        import json

                        if text.strip().startswith("{") or text.strip().startswith("["):
                            data = json.loads(text)
                            if isinstance(data, dict):
                                lines = []
                                for k, v in data.items():
                                    lines.append(f"- {k}: {v}")
                                return "\n".join(lines)
                            if isinstance(data, list):
                                return "\n".join(f"- {item}" for item in data)
                    except Exception:
                        pass
                    return text
                except Exception as inner_e:
                    last_err = inner_e
                    continue
            if last_err is not None:
                return f"ERROR from Gemini: {last_err}"
            return "(prazan odgovor)"
        except Exception as e:
            return f"ERROR from Gemini: {e}"
    return (gemini_summarize,)


@app.cell
def _(
    gemini_summarize,
    google_key,
    run_btn,
    steel_fetch_text,
    steel_key,
    url_input,
):
    import marimo as _mo
    view = _mo.md("Unesite URL i kliknite ‘Scrape & summarize’.")
    if run_btn.value:
        url = (url_input.value or "").strip()
        if not url:
            view = _mo.md("Please enter a URL.")
        elif not steel_key or not google_key:
            view = _mo.md("Missing STEEL_API_KEY or GOOGLE_API_KEY in .env")
        else:
            steel_text = steel_fetch_text(url, steel_key)
            if not isinstance(steel_text, str):
                steel_text = str(steel_text)
            excerpt = (steel_text or "").strip().replace("\n", " ")[:500]
            llm_out = gemini_summarize(
                excerpt, google_key) if excerpt else "(nema teksta)"
            view = _mo.md(
                f"**Scraped URL:** {url}\n\n"
                f"**Steel output (isječak, ~500 znakova):**\n\n{excerpt}\n\n"
                f"**LLM rezultat:**\n\n{llm_out}"
            )

    view
    return


if __name__ == "__main__":
    app.run()
