import json
import os
import subprocess
import sys
from datetime import datetime

# Auto-install requirements if not available
try:
    import requests
except ImportError:
    print("Installing required packages...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests

class FBrefScraper:
    def __init__(self, steel_api_key, gemini_api_key):
        """
        Initialize the FBref scraper with Steel API and Gemini API

        Args:
            steel_api_key: Your Steel API key from https://app.steel.dev
            gemini_api_key: Your Google Gemini API key
        """
        self.steel_api_key = steel_api_key
        self.steel_api_url = "https://api.steel.dev/v1/scrape"
        self.gemini_api_key = gemini_api_key
        self.gemini_api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={gemini_api_key}"

    def fetch_with_steel_api(self, fbref_url):
        """
        Fetch content from FBref using Steel API

        Args:
            fbref_url: The FBref match URL to scrape

        Returns:
            The text content from the page
        """
        print(f"Fetching data from: {fbref_url}")
        print("Using Steel API...")

        try:
            # Correct Steel API headers (note: steel-api-key, not x-steel-api-key)
            headers = {
                "Content-Type": "application/json",
                "steel-api-key": self.steel_api_key
            }

            # Use the direct scrape endpoint
            scrape_payload = {
                "url": fbref_url
            }

            print(f"Scraping {fbref_url}...")
            scrape_response = requests.post(
                "https://api.steel.dev/v1/scrape",
                json=scrape_payload,
                headers=headers,
                timeout=120
            )

            if scrape_response.status_code == 200:
                data = scrape_response.json()
                # Debug: print the response structure
                print(f"Response keys: {list(data.keys())}")

                # Steel API returns content in different fields
                content = data.get('content') or data.get('body') or data.get('html') or data.get('data') or str(data)

                if isinstance(content, str):
                    print(f"Successfully fetched {len(content)} characters from Steel API")
                else:
                    print(f"Content type: {type(content)}")
                    content = str(content)

                return content
            else:
                print(f"Steel API returned status code: {scrape_response.status_code}")
                print(f"Response: {scrape_response.text}")
                return None

        except Exception as e:
            print(f"Error fetching from Steel API: {str(e)}")
            return None

    def process_with_gemini(self, text_content, prompt=None):
        """
        Send the scraped text to Google Gemini API for processing

        Args:
            text_content: The text content to process
            prompt: Optional custom prompt for Gemini

        Returns:
            Gemini's response
        """
        if prompt is None:
            prompt = """You are analyzing football match data scraped from FBref.

Write a concise 300-word explanation of this match data. Your explanation should:
- Summarize the key match details (teams, score, date, competition)
- Highlight the most important statistics and what they reveal about the match
- Mention standout player performances if visible in the data
- Discuss key moments or turning points in the match
- Keep it informative but conversational

Limit your response to approximately 300 words."""

        print("\nSending data to Google Gemini API for analysis...")

        try:
            # Ensure text_content is a string
            if not isinstance(text_content, str):
                text_content = str(text_content)

            # Limit content to 50k chars to avoid API limits
            limited_content = text_content[:50000] if len(text_content) > 50000 else text_content

            # Prepare the request for Gemini API
            payload = {
                "contents": [{
                    "parts": [{
                        "text": f"{prompt}\n\nMatch Data:\n{limited_content}"
                    }]
                }],
                "generationConfig": {
                    "temperature": 0.4,
                    "topK": 32,
                    "topP": 1,
                    "maxOutputTokens": 4096,
                }
            }

            response = requests.post(
                self.gemini_api_url,
                json=payload,
                headers={"Content-Type": "application/json"},
                timeout=60
            )

            if response.status_code == 200:
                result = response.json()
                # Extract the generated text from Gemini's response
                if 'candidates' in result and len(result['candidates']) > 0:
                    gemini_response = result['candidates'][0]['content']['parts'][0]['text']
                    print("Successfully received response from Gemini API")
                    return gemini_response
                else:
                    print("Unexpected response structure from Gemini API")
                    return None
            else:
                print(f"Gemini API returned status code: {response.status_code}")
                print(f"Response: {response.text}")
                return None

        except Exception as e:
            print(f"Error processing with Gemini API: {str(e)}")
            return None

    def scrape_and_analyze(self, fbref_url, scraped_data_file="scraped_data.md", analysis_file="match_analysis.md"):
        """
        Complete workflow: Fetch from FBref using Steel API, then analyze with Gemini

        Args:
            fbref_url: The FBref match URL
            scraped_data_file: File to save the raw scraped data (default: scraped_data.md)
            analysis_file: File to save the Gemini analysis (default: match_analysis.md)

        Returns:
            Dictionary containing the results
        """
        # Step 1: Fetch content using Steel API
        raw_content = self.fetch_with_steel_api(fbref_url)

        if not raw_content:
            print("Failed to fetch content from FBref")
            return None

        # Save raw scraped data to file
        with open(scraped_data_file, 'w', encoding='utf-8') as f:
            f.write(f"# Scraped Data from FBref\n\n")
            f.write(f"**URL:** {fbref_url}\n")
            f.write(f"**Timestamp:** {datetime.now().isoformat()}\n\n")
            f.write("---\n\n")
            f.write(raw_content)
        print(f"\nRaw scraped data saved to: {scraped_data_file}")

        # Step 2: Process with Gemini API
        gemini_analysis = self.process_with_gemini(raw_content)

        if not gemini_analysis:
            print("Failed to process content with Gemini API")
            return None

        # Prepare results
        results = {
            "url": fbref_url,
            "timestamp": datetime.now().isoformat(),
            "raw_content_length": len(raw_content),
            "gemini_analysis": gemini_analysis,
            "scraped_data_file": scraped_data_file,
            "analysis_file": analysis_file
        }

        # Save Gemini analysis to file
        with open(analysis_file, 'w', encoding='utf-8') as f:
            f.write(f"# Match Analysis\n\n")
            f.write(f"**URL:** {fbref_url}\n")
            f.write(f"**Timestamp:** {results['timestamp']}\n\n")
            f.write("---\n\n")
            f.write(gemini_analysis)
        print(f"Gemini analysis saved to: {analysis_file}")

        return results


def main():
    """
    Main function to run the scraper
    """
    # Example FBref match URL (Champions League Final 2023)
    # You can change this to any FBref match URL
    match_url = "https://fbref.com/en/matches/633d3171/Pafos-FC-Villarreal-November-5-2025-Champions-League"

    # Get Steel API key from environment variable or input
    steel_api_key = os.environ.get('STEEL_API_KEY')

    if not steel_api_key:
        print("Please enter your Steel API key:")
        print("(Get it from: https://app.steel.dev)")
        steel_api_key = input("Steel API Key: ").strip()

    if not steel_api_key:
        print("Error: Steel API key is required!")
        return

    # Get Gemini API key from environment variable or input
    gemini_api_key = os.environ.get('GEMINI_API_KEY')

    if not gemini_api_key:
        print("\nPlease enter your Google Gemini API key:")
        print("(Get it from: https://makersuite.google.com/app/apikey)")
        gemini_api_key = input("Gemini API Key: ").strip()

    if not gemini_api_key:
        print("Error: Gemini API key is required!")
        return

    # Create scraper instance
    scraper = FBrefScraper(steel_api_key, gemini_api_key)

    # Run the scraper
    print("\n" + "=" * 60)
    print("FBref Match Scraper with Steel API + Google Gemini")
    print("=" * 60)
    print()

    results = scraper.scrape_and_analyze(
        fbref_url=match_url,
        scraped_data_file="scraped_data.md",
        analysis_file="match_analysis.md"
    )

    if results:
        print("\n" + "=" * 60)
        print("SCRAPING COMPLETE!")
        print("=" * 60)
        print(f"\n✓ Raw scraped data: {results['scraped_data_file']}")
        print(f"✓ Gemini analysis: {results['analysis_file']}")
        print("\n" + "=" * 60)
        print("GEMINI ANALYSIS (Copy this for your PR):")
        print("=" * 60)
        print()
        print(results['gemini_analysis'])
        print()
        print("=" * 60)
    else:
        print("\nScraping failed. Please check the error messages above.")


if __name__ == "__main__":
    main()
