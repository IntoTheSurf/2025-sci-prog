# Simulation System Specification for Modeling User Interactions with Advertisements

## 1. Project Structure

```
config/
├── simulation_config.yaml        ← global simulation settings

data/
├── users.json                    ← description of all agents
├── ads.json                      ← description of all advertisements
└── interactions.db               ← database of recorded interactions (DuckDB)

agents/
├── agent.py                      ← Agent class implementation
└── memory_manager.py             ← agent cache and memory management

world/
├── simulator.py                  ← orchestration of simulation iterations and ad allocation
└── logger.py                     ← logging all events and interactions to database

models/
└── decision_model.py             ← machine learning model for behavior prediction

main.py                           ← application entry point (starts simulation)
```

## 2. Entities

### 2.1 Advertisements

#### 2.1.1 Features

Each advertisement is defined by a set of descriptive features that serve as input to the model and prompt to the agent:

| Feature | Description |
|---------|-------------|
| theme | thematic category of the advertisement (e.g., sport, fashion, technology) |
| color tone | dominant tonality and color contrast |
| rhetorical triangle | which is most dominant - emotional, logical, or ethical dimension of the message |
| text amount | generally no text, contains title/product name, contains title/name and bullet points, contains paragraph of text |

Features can be extracted from image data using computer vision or manual annotation.

**Possible sources:**
- (a) existing Kaggle datasets with advertisements (select those with relevant text and images)
- (b) scraping or unofficial social media APIs

Each advertisement additionally contains:
- day of entry into simulation
- interaction rate, calculated as:

```
interaction_rate = [(click + share + 2·like) - (2·dislike + ignore)] / N
```

where N is the number of users who interacted.

When the interaction rate falls below a defined threshold, the advertisement is deactivated and no longer displayed.

### 2.2 Users (Agents)

#### 2.2.1 Agent Implementation

Each agent represents one user and is defined using two groups of features:

**Personal features:**
- age
- family
- gender
- hobbys
- profession

📘 **Data source:** RedDust dataset — it is necessary to process and consolidate the features of each user into a unique JSON record.

**Propensity features:**
- activity_level – propensity to react to content
- risk_tolerance – propensity to try new advertisements
- social_engagement – probability of sharing content

Values are assigned randomly, in percentages (0–100%), as an abstract description of behavior, not as a measurement of actual interactions.

Agents have access to their interaction history through the memory manager, which enables insight into their own previous reactions without the need to repeatedly fetch all records from the database.

The complete description of agents is stored in the `users.json` file.

## 3. User and Advertisement Interaction

### 3.1 Advertisement Selection

After the model calculates the probability of positive reaction for each user group and each advertisement:

1. Advertisements with probability greater than 30% are filtered
2. Advertisements are distributed according to the ratio of their probabilities, so that they total the number of displays in one simulation day
3. From each user group, a number of agents is randomly selected proportional to the assigned number of displays

### 3.2 Advertisement Exposure to Agent

The query sent to the agent contains:
- agent description
- advertisement description
- descriptive metrics of the agent's reaction history, which can be represented in three ways:

| Option | Description | Advantage / Disadvantage |
|--------|-------------|-------------------------|
| (a) Vector representation | user represented as an embedding based on behavior | compressive, fast, flexible |
| (b) Sending entire history | agent receives detailed interaction log | precise, but slow and expensive |
| (c) Aggregated metrics | averages of interactions with advertisements that share features with the current advertisement | simple and efficient |

This is yet to be decided

### 3.3 Agent Response (Interaction)

The agent can select one or more actions:

`ignore, click, like, dislike, share`

Mutual compatibility constraints are defined by the following rules:

```json
{
  "ignore": ["share"],
  "click": ["like", "dislike", "share"],
  "like": ["click", "share"],
  "dislike": ["click", "share"],
  "share": ["like", "dislike", "click"]
}
```

The result of each interaction is recorded as a JSON object with binary values (true / false) for each action.

All records after cleaning are stored in the DuckDB database (`interactions.db`).

## 4. Model

> **Note:** Specific algorithms and other details are still not well defined here. This part will be worked out through the Machine Learning course.

### 4.1 User Clustering

Users are grouped using unsupervised algorithms (e.g., K-Means, DBSCAN, hierarchical clustering).

The resulting groups are subsequently manually interpreted and labeled (e.g., sports types, influencers, passive users).

### 4.2 Behavior Learning

The model learns from interactions stored in the database, which are updated after each simulation day.

- **Input data:** user features + advertisement features
- **Output:** predicted probability of positive interaction

**Recommended algorithms:**
- regression models (e.g., logistic regression)
- decision trees / random forest
- possibly gradient boosting (if performance requires it)

### 4.3 Evaluation and Visualization

Evaluation begins after sufficient data has accumulated (e.g., after 10 simulation days).

Part of each day's interactions is used as a test set.

**Evaluation metrics:**
- MAE or RMSE by user groups
- visualizations of interaction trends over time (CTR, engagement rate, etc.)

### 4.4 Prediction

For each new advertisement, the model:

1. iterates through all users within one group
2. calculates the predicted interaction probability
3. aggregates results into the group's average value
4. records results in JSON format:

```json
{
  "sports_types": 0.72,
  "tech_enthusiasts": 0.56,
  "passive": 0.19
}
```

## 5. Simulation Environment

Defined by JSON object:

```json
{
  "simulation_days": 100,
  "agents_count": 100,
  "ads_count": 50,
  "llm_model": "gpt-4-mini",
  "decision_temperature": 0.7,
  "no_agents_exposed_to_ad": 10,
  "actions": ["click", "like", "dislike", "ignore", "share"],
  "action_compatibility": {
    "ignore": ["share"],
    "click": ["like", "dislike", "share"],
    "like": ["click", "share"],
    "dislike": ["click", "share"],
    "share": ["like", "dislike", "click"]
  },
  "update_frequency": "daily",
  "seed": 42,
  "evaluation_starting_day": 10
}
```

## 6. Simulation Flow

1. **Agent and advertisement initialization**
2. **Loading existing model** (if exists)
3. **For each simulation day:**
   - Generating advertisement display schedule
   - Executing interactions (model/LLM → agent reaction)
   - Recording results in DuckDB
   - Updating agent states
   - Retraining the model
4. **Upon completion:**
   - Generating performance reports and visualizations