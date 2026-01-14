# 📚 Scripts MLflow pour le Cours DevMLOps

Ce dossier contient une série de scripts pédagogiques pour apprendre à utiliser MLflow dans un contexte de DevMLOps.

## 🎯 Objectifs du cours

Apprendre aux étudiants à:
- ✅ Monitorer leurs modèles de Machine Learning
- ✅ Enregistrer et versionner leurs modèles
- ✅ Télécharger automatiquement la dernière version d'un modèle
- ✅ Détecter le data drift
- ✅ Comparer les performances de différents modèles

## 📋 Scripts disponibles

### 1️⃣ **mlflow_01_basic_logging.py** - Enregistrement basique
**Concepts abordés:**
- Logger des paramètres (hyperparamètres)
- Logger des métriques (accuracy, f1-score, etc.)
- Logger un modèle entraîné
- Logger des artefacts (graphiques, fichiers)
- Utiliser des tags pour organiser les runs

**Utilisation:**
```bash
python mlflow_01_basic_logging.py
```

---

### 2️⃣ **mlflow_02_model_registry.py** - Model Registry & Versioning
**Concepts abordés:**
- Enregistrer un modèle dans le Model Registry
- Gérer les versions de modèles
- Changer les stages (None → Staging → Production → Archived)
- Ajouter des descriptions et tags aux versions
- Comparer automatiquement les performances entre versions

**Utilisation:**
```bash
python mlflow_02_model_registry.py
```

---

### 3️⃣ **mlflow_03_load_latest_model.py** - Chargement de modèles
**Concepts abordés:**
- Charger un modèle par stage (Production, Staging)
- Charger une version spécifique
- Charger la dernière version entraînée
- Charger depuis un Run ID
- Utiliser le modèle pour faire des prédictions

**Utilisation:**
```bash
# D'abord, exécutez le script 2 pour créer des modèles
python mlflow_02_model_registry.py

# Puis chargez le modèle
python mlflow_03_load_latest_model.py
```

---

### 4️⃣ **mlflow_04_parameter_tuning.py** - Monitoring & Hyperparameter Tuning
**Concepts abordés:**
- Entraîner plusieurs modèles avec différents hyperparamètres
- Logger et comparer les performances
- Utiliser des runs parents/enfants pour organiser les expérimentations
- Trouver automatiquement le meilleur modèle
- Utiliser l'API de recherche MLflow

**Utilisation:**
```bash
python mlflow_04_parameter_tuning.py
```

**Note:** Ce script peut prendre quelques minutes (teste 48 combinaisons d'hyperparamètres).

---

### 5️⃣ **mlflow_05_data_drift_detection.py** - Détection de Data Drift
**Concepts abordés:**
- Détecter les changements dans la distribution des données
- Calculer le Population Stability Index (PSI)
- Utiliser le test de Kolmogorov-Smirnov
- Comparer les statistiques entre train et production
- Créer des visualisations de drift
- Alerter en cas de drift significatif

**Utilisation:**
```bash
python mlflow_05_data_drift_detection.py
```

---

## 🚀 Ordre d'exécution recommandé

Pour une expérience d'apprentissage optimale:

1. **Démarrez avec le script 1** pour comprendre les bases du logging
2. **Passez au script 2** pour voir comment gérer les versions
3. **Exécutez le script 3** pour apprendre à charger des modèles
4. **Testez le script 4** pour comparer des modèles
5. **Finissez avec le script 5** pour la détection de drift

## 📊 Visualisation dans MLflow UI

Après avoir exécuté les scripts, consultez l'interface MLflow:

```
http://localhost:5000
```

### Navigation dans l'UI:

- **Experiments** 📂 : Voir tous vos runs organisés par expérience
- **Models** 🏷️ : Consulter le registry et les versions de modèles
- **Compare** ⚖️ : Comparer plusieurs runs côte à côte
- **Charts** 📈 : Visualiser les métriques sous forme de graphiques

## 💡 Bonnes pratiques enseignées

### 1. Organisation des expériences
```python
mlflow.set_experiment("nom_descriptif")
```

### 2. Nommage des runs
```python
with mlflow.start_run(run_name="description_claire"):
```

### 3. Logging structuré
```python
# Paramètres: configuration du modèle
mlflow.log_params({"n_estimators": 100, "max_depth": 5})

# Métriques: résultats quantitatifs
mlflow.log_metrics({"accuracy": 0.95, "f1_score": 0.93})

# Tags: métadonnées qualitatives
mlflow.set_tags({"team": "data-science", "environment": "prod"})
```

### 4. Gestion des versions en production
```python
# En production, toujours utiliser le stage
model_uri = "models:/model_name/Production"
model = mlflow.sklearn.load_model(model_uri)
```

### 5. Monitoring continu
- Logger les performances en production
- Détecter le data drift régulièrement
- Automatiser le ré-entraînement si drift > seuil

## 🛠️ Configuration

Tous les scripts utilisent le même serveur MLflow:
```python
mlflow.set_tracking_uri("http://localhost:5000")
```

Pour utiliser un serveur différent, modifiez cette ligne dans chaque script.

## 📦 Dépendances

```bash
pip install mlflow scikit-learn matplotlib numpy scipy
```

## 🎓 Exercices pour les étudiants

### Exercice 1: Modifier les paramètres
Modifiez `mlflow_04_parameter_tuning.py` pour tester d'autres algorithmes (SVM, KNN, etc.).

### Exercice 2: Ajouter des métriques
Dans `mlflow_01_basic_logging.py`, ajoutez le logging de nouvelles métriques (recall, ROC-AUC, etc.).

### Exercice 3: Monitoring en temps réel
Créez un script qui charge le modèle en production et surveille ses performances en continu.

### Exercice 4: Alertes automatiques
Modifiez `mlflow_05_data_drift_detection.py` pour envoyer une alerte (email, Slack) en cas de drift.

### Exercice 5: CI/CD Pipeline
Intégrez ces scripts dans un pipeline CI/CD (GitHub Actions, GitLab CI, etc.).

## 🔗 Ressources additionnelles

- [Documentation MLflow](https://mlflow.org/docs/latest/index.html)
- [MLflow Model Registry](https://mlflow.org/docs/latest/model-registry.html)
- [Evidently AI (drift detection)](https://www.evidentlyai.com/)
- [Great Expectations](https://greatexpectations.io/)

## 📝 Notes pédagogiques

### Points clés à souligner:

1. **Reproductibilité**: MLflow garantit que les expériences sont reproductibles
2. **Traçabilité**: Chaque run est enregistré avec tous ses paramètres
3. **Collaboration**: L'équipe peut voir et comparer les résultats
4. **Production-ready**: Le Model Registry facilite le déploiement
5. **Gouvernance**: Les stages permettent de contrôler ce qui est déployé

### Erreurs communes à éviter:

❌ Ne pas logger les paramètres → impossible de reproduire
❌ Ne pas versionner les modèles → confusion sur ce qui est déployé
❌ Ignorer le data drift → dégradation silencieuse des performances
❌ Ne pas tester avant de promouvoir en Production
❌ Oublier de documenter les modèles (descriptions, tags)

## 🤝 Support

Pour toute question sur les scripts ou MLflow:
- Consultez la documentation MLflow
- Posez des questions pendant le cours
- Expérimentez et testez différentes configurations!

---

**Bon apprentissage! 🚀📊🤖**
