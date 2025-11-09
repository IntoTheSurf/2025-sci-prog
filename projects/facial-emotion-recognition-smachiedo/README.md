# Facial Emotion Recognition - Srđan Machiedo

**Project:** Facial Emotion Recognition
**Student:** Srđan Machiedo
**Status:** In Progress

## 🎯 Project Overview

Cilj projekta je razviti sustav koji može prepoznati emocije na ljudskom licu koristeći slike.    

Problem koji rješavam je **kako trenirati model koji može točno prepoznati osnovne emocije**  
(sreća, tuga, ljutnja, iznenađenje, strah, gađenje i neutralno) koristeći skup slika lica.

---

## 💡 Hipoteza
Ako neuronska mreža nauči dovoljno reprezentativne obrasce lica (npr. osmijeh, podignute obrve, namrgođeno čelo),  
moći će točno prepoznati emocije i na slikama koje prethodno nije vidjela.  

---

## 📊 Podaci
Koristim **FER2013 dataset**, dostupan na [Kaggleu](https://www.kaggle.com/datasets/msambare/fer2013).  
- Sadrži oko **35.000 crno-bijelih slika lica** (48×48 piksela).  
- Svaka slika ima oznaku emocije (0–6) koja odgovara jednoj od sedam kategorija:  
  - 😠 **Ljutnja**  
  - 🤢 **Gađenje**  
  - 😨 **Strah**  
  - 🙂 **Sreća**  
  - 😞 **Tuga**  
  - 😲 **Iznenađenje**  
  - 😐 **Neutralno**  
- Podaci su organizirani u CSV datoteci s tri stupca:  
  - `emotion` — oznaka emocije (0–6)  
  - `pixels` — niz vrijednosti piksela slike  
  - `Usage` — oznaka je li slika dio train, validation ili test skupa  

---

## ⚙️ Metodologija i pristup
1. **Učitavanje i obrada podataka**  
   - Parsiranje `pixels` polja u 48×48 slike  
   - Normalizacija vrijednosti piksela (0–1)  
   - One-hot encoding emocija  

2. **Izgradnja i treniranje modela**  
   - Jednostavna **neuronska mreža (CNN)** koja uči prepoznati obrasce lica  

3. **Evaluacija performansi**  
   - Graf točnosti i gubitka kroz epohe  
   - Matrica konfuzije za analizu pogrešaka  

4. **Predikcija novih slika**  
   - Testiranje modela na slikama koje nisu bile u skupu za treniranje  

5. **(Opcionalno)** Real-time prepoznavanje emocija pomoću web kamere  
   - Pomoću `OpenCV` biblioteke  

## 👤 Student Information

- **Student Name**: Srđan Machiedo
- **GitHub**: @Machiedo81

## 🛠 Technologies Used

- Language: Python
- Dataset: FER2013 from kaggle.com
- TBD
- 

## 🚀 Getting Started

### For Development

1. **Clone the repository**:
   ```bash
   git clone [your-fork-url]
   cd 2025-sci-prog/projects/[projectname-student]
   ```

2. **Set up your environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Create your feature branch**:
   ```bash
   git checkout -b feature/[feature-name]
   ```

### For Instructors/Reviewers

1. View project documentation below
2. Check GitHub Issues for project planning
3. Review Pull Requests for development process

## 🔄 Development Workflow

### Daily Routine

1. **Start of Session (5 minutes)**
   - Review your goals for the session
   - Pull latest changes: `git pull origin main`
   - Create feature branch: `git checkout -b feature/[feature-name]`

2. **During Development**
   - **Write code** incrementally and test frequently
   - **Commit often** with descriptive messages
   - **Document your process** and decisions

3. **End of Session (10 minutes)**
   - **Push your branch**: `git push origin feature/[feature-name]`
   - **Create Pull Request** to main branch
   - **Review your own work** before merging

### Branch Strategy

- `main`: Protected branch for final, working code
- `feature/[feature-name]`: Individual feature branches
- All work happens on feature branches, never directly on main

### Pull Request Process

1. **Create PR** from feature branch to main
2. **Self-review** your changes carefully
3. **Use the PR template** (see below)
4. **Merge only after** testing and documentation is complete

## 📝 Pull Request Template

```markdown
## What I Did
- [ ] Feature 1 implemented
- [ ] Feature 2 implemented
- [ ] Tests added and passing
- [ ] Documentation updated

## How to Test
1. Run `python main.py` (or appropriate test command)
2. Expected output: ...

## What I Learned
- Brief reflection on what you learned during this session

## Next Steps
- What you plan to work on next
```

## 🛠 Development Best Practices

### Code Quality
- **Test your code** before committing
- **Write clear commit messages** following conventional commits
- **Add comments** where code is complex or non-obvious
- **Refactor regularly** to improve code structure

### Problem Solving
- **Research solutions** - don't waste time being stuck
- **Draw diagrams** to visualize complex problems
- **Document your approach** and reasoning
- **Ask for help** from instructors when needed

## 📊 Project Requirements

### Technical Requirements ✅
- [ ] Use appropriate programming language for your project
- [ ] Include proper error handling
- [ ] Add comments and documentation
- [ ] Create tests for major functionality
- [ ] Use Git appropriately (commits, branches, PRs)

### Documentation Requirements ✅
- [ ] Document your development process
- [ ] Explain your approach and decisions
- [ ] Include setup instructions
- [ ] Document any challenges faced and solutions found

## 📈 Project Progress

### Completed Tasks
- [ ] Project setup and repository structure
- [ ] Environment configuration
- [ ] Initial research/planning

### In Progress
- [ ] Core functionality implementation
- [ ] Testing and debugging

### Next Steps
- [ ] Documentation and refinement
- [ ] Final testing and cleanup
- [ ] Presentation/demonstration preparation

## 🐛 Issues & Challenges

### Current Challenges
- [Document any current challenges or blockers]

### Solutions Tried
- [Document solutions you've attempted]

## 📚 Resources Used

- [Relevant documentation, tutorials, papers, etc.]
- [Tools or libraries you found helpful]

## 🤝 How to Use This Template

1. **Copy this folder** and rename it: `projectname-yourusername/`
2. **Update this README** with your project information
3. **Replace project details** with your specific project
4. **Customize the technologies** and requirements as needed
5. **Start developing** using the workflow above!

---

## ❓ Need Help?

- **Create a GitHub Issue** in the main repository
- **Ask during class** or office hours
- **Review documentation** for workflow questions
- **Check other project folders** for examples

**Remember**: The goal is to learn technical skills AND good development practices. Take pride in your work and document your learning journey!
