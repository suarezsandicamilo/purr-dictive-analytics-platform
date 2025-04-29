# Purr-dictive Analytics Platform

## Project Description

The **Purr-dictive Analytics Platform** aims to develop a scalable system capable of ingesting and processing large datasets to generate predictive insights using machine learning algorithms. Initially, the focus is on [**The Complete Pokémon Dataset**](https://www.kaggle.com/datasets/rounakbanik/pokemon/data), which provides data on over 800 Pokémon from the first seven generations, including base stats, types, and other categorical features. The platform will implement predictive models to classify Pokémon types and estimate overall strength based on their attributes. For scalability and reliability, the platform leverages containerization (Docker) for cloud deployment (AWS, Azure, or GCP) and utilizes PostgreSQL for efficient data storage.

## Technologies Used

- **Programming Language:** Python
- **AI/ML Libraries:** scikit-learn, TensorFlow, PyTorch
- **Cloud Providers:** AWS, Azure, GCP
- **Database:** PostgreSQL
- **DevOps Tools:** Docker

## Dataset

- **Primary Dataset:** [**The Complete Pokémon Dataset**](https://www.kaggle.com/datasets/rounakbanik/pokemon/data)

## Exploratory Data Analysis (EDA)

Initial data exploration focuses on understanding the characteristics of the Pokémon dataset, including:

- Examining distributions of Pokémon attributes such as types, stats (HP, Attack, Defense, Speed, etc.), and generations.
- Identifying correlations between features, exploring how type combinations and stat distributions influence overall strength.

## Model Training

The platform will implement and train machine learning models to generate predictive insights:

- **Classification Models:** Predict Pokémon primary/secondary types and legendary status based on attributes such as base stats and generation.
- **Regression Models:** Estimate overall Pokémon strength (e.g., total base stats) using features like Attack, Defense, Speed, and special stats.

## Deployment

The platform aims to deliver valuable interactive Pokémon analytics through:

- **Real-time Dashboard:** A web dashboard that visualizes Pokémon distributions (by type, generation, base stats) and displays model predictions for type classification and strength estimation, with interactive filters for browsing the dataset.
- **RESTful API:** An API that accepts Pokémon attributes as input and returns predicted classifications (e.g., type, legendary status) or strength scores. The API supports integration with external applications and the dashboard.
- **Containerized Deployment:** Using Docker to containerize the dashboard, API, and model components for consistent environments. Deployment will target a cloud provider (AWS, Azure, or GCP) to ensure scalability and high availability.

## Directory Structure

```
purr_dictive_analytics/
├── data/
│   └── processed/
├── notebooks/
│   └── exploratory_data_analysis.ipynb
├── models/
│   ├── training/
│   └── deployment/
├── src/
│   ├── data_processing/
│   ├── model_training/
│   └── api/
├── tests/
│   ├── data_processing/
│   ├── model_training/
│   └── api/
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
└── requirements.txt
```

### Description of Directory Structure

- `data/`: Transformed (processed) datasets for analysis and model training.
- `notebooks/`: Jupyter notebooks for exploratory data analysis and model experimentation.
- `models/`: Trained machine learning models, including training and deployment scripts.
- `src/`: Core application code organized into modules for data processing, model training, and API services.
- `tests/`: Unit and integration tests for modules in the `src` directory, ensuring code quality.
- `docker/`: Docker configuration files (`Dockerfile`, `docker-compose.yml`) for containerization and orchestration.
- `requirements.txt`: Lists Python dependencies needed to run the project.
