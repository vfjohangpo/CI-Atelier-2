
## Le projet

Une petite API REST qui gère des *items*. Le code est volontairement simple — l'intérêt est dans le **pipeline**, pas dans l'application.

| Endpoint | Méthode | Description |
|----------|---------|-------------|
| `GET /health` | GET | Health check |
| `GET /version` | GET | Version de l'API |
| `GET /items` | GET | Liste des items |
| `POST /items` | POST | Crée un item |
| `GET /items/{id}` | GET | Détail d'un item |
| `DELETE /items/{id}` | DELETE | Supprime un item |

**Stack** : Python 3.12, FastAPI, pytest, ruff, httpx.

## Comment utiliser ce dépôt

### 1. Clonez votre fork

```bash
# Remplacez <votre-pseudo> par votre nom d'utilisateur GitLab
git clone git@gitlab.com:<votre-pseudo>/pipeline-craft.git
cd pipeline-craft
```

### 3. Lisez le guide, puis le lab

Chaque lab est adossé à un **guide** sur le site. Avant de coder :

1. **Lisez le guide lié** — il pose les concepts (lien dans le tableau ci-dessous).
2. **Ouvrez la page du lab** sur [blog.stephane-robert.info/docs/pipeline-cicd/gitlab/labs/](https://blog.stephane-robert.info/docs/pipeline-cicd/gitlab/labs/) — elle contient les consignes précises, les étapes et les critères de réussite.
3. **Revenez ici** pour coder.

> **Guide (théorie) → Page du lab (consignes) → Repo (pratique)**

### 4. Basculez sur la branche du lab

Chaque lab a deux branches :

| Branche | Rôle |
|---------|------|
| `starter/lab-XX` | Point de départ — c'est ici que vous codez |
| `solution/lab-XX` | Correction complète — à consulter si vous bloquez |

```bash
# Exemple : commencer le Lab 01
git checkout starter/lab-01
```

### 5. Codez, poussez, vérifiez

Suivez les consignes du lab, modifiez les fichiers, puis :

```bash
git add -A
git commit -m "ci: solution lab 01"
git push origin starter/lab-01
```

Allez dans **Build > Pipelines** sur votre projet GitLab pour voir le résultat.

### 6. Si vous bloquez

Comparez votre travail avec la solution :

```bash
git diff starter/lab-01..solution/lab-01
```

Ou basculez directement sur la correction :

```bash
git checkout solution/lab-01
```

### Résumé visuel

💻 Ce dépôt (votre fork)           ← coder la solution
        │
        ├── git checkout starter/lab-XX   ← point de départ
        ├── … codez, committez, poussez …
        └── git checkout solution/lab-XX  ← correction si besoin
```

## Les 26 labs

### Bloc 1 — Fondamentaux (Labs 01–11)

Du premier pipeline à un pipeline complet avec validation, registries, rapports qualité et diagnostic avancé.

| Lab | Titre | Compétence | Guide lié |
|-----|-------|------------|-----------|
| 01 | Mon premier pipeline | Écrire un `.gitlab-ci.yml` à 3 stages | [Premier pipeline](https://blog.stephane-robert.info/docs/pipeline-cicd/gitlab/fondamentaux/premier-pipeline/) |
| 02 | Lire un échec | Diagnostiquer un job rouge via les logs | [Debug logs](https://blog.stephane-robert.info/docs/pipeline-cicd/gitlab/fondamentaux/debug-logs/) |
| 03 | Images et runners | Choisir les bonnes images, Docker-in-Docker | [Runners](https://blog.stephane-robert.info/docs/pipeline-cicd/gitlab/fondamentaux/runners/) |
| 04 | Artifacts et cache | Transmettre des fichiers entre jobs | [Artifacts et cache](https://blog.stephane-robert.info/docs/pipeline-cicd/gitlab/fondamentaux/artifacts-cache/) |
| 05 | Sortir les secrets du code | Variables CI/CD protégées, masquage | [Variables](https://blog.stephane-robert.info/docs/pipeline-cicd/gitlab/fondamentaux/variables/) |
| 06 | Contrôler l'exécution | `rules:`, `workflow: rules`, déploiement conditionnel | [Rules](https://blog.stephane-robert.info/docs/pipeline-cicd/gitlab/fondamentaux/rules/) |
| 07 | Valider un pipeline | `glab ci lint`, CI Lint UI, pré-validation | [Valider un .gitlab-ci.yml](https://blog.stephane-robert.info/docs/pipeline-cicd/gitlab/fondamentaux/validation-pipeline/) |
| 08 | Déclencher un pipeline | Schedules, trigger tokens, API | [Déclencheurs](https://blog.stephane-robert.info/docs/pipeline-cicd/gitlab/fondamentaux/declencheurs/) |
| 09 | Publier dans le registry | Container Registry, Package Registry | [Registries](https://blog.stephane-robert.info/docs/pipeline-cicd/gitlab/fondamentaux/registries/) |
| 10 | Rapports qualité | JUnit, coverage, badge dans la MR | [Rapports qualité](https://blog.stephane-robert.info/docs/pipeline-cicd/gitlab/fondamentaux/rapports-qualite/) |
| 11 | Débugger un job bloqué | Diagnostic pending/skipped, tags runner | [Debug pending](https://blog.stephane-robert.info/docs/pipeline-cicd/gitlab/fondamentaux/debug-pending/), [Debug skipped](https://blog.stephane-robert.info/docs/pipeline-cicd/gitlab/fondamentaux/debug-skip/) |

### Bloc 2 — Industrialisation (Labs 12–19)

Cache avancé, DRY, templates, parallélisme, DAG et pipelines parent/enfant.

| Lab | Titre | Compétence | Guide lié |
|-----|-------|------------|-----------|
| 12 | Accélérer le pipeline | Cache `hashfiles`, images slim, `needs:`, DAG | [DAG et parallélisme](https://blog.stephane-robert.info/docs/pipeline-cicd/gitlab/industrialisation/dag-parallelisme/) |
| 13 | DRY : extends et anchors | Factoriser le YAML avec `extends:` et ancres | [Extends et anchors](https://blog.stephane-robert.info/docs/pipeline-cicd/gitlab/industrialisation/extends-anchors/) |
| 14 | Templates partagés | `include:` local, project, remote | [Templates](https://blog.stephane-robert.info/docs/pipeline-cicd/gitlab/industrialisation/templates/) |
| 15 | Matrices multi-versions | `parallel:matrix` Python 3.11/3.12 | [Matrices](https://blog.stephane-robert.info/docs/pipeline-cicd/gitlab/industrialisation/matrices/) |
| 16 | Pipeline parent-enfant | `trigger:include`, pipelines dynamiques | [Parent-enfant](https://blog.stephane-robert.info/docs/pipeline-cicd/gitlab/industrialisation/parent-enfant/) |
| 17 | Workflows branches et MR | MR pipelines, merge trains, release flow | [Workflows](https://blog.stephane-robert.info/docs/pipeline-cicd/gitlab/industrialisation/workflows/) |
| 18 | Fiabilité et retry | `retry:`, `timeout:`, `interruptible:` | [Fiabilité](https://blog.stephane-robert.info/docs/pipeline-cicd/gitlab/industrialisation/fiabilite/) |
| 19 | Capstone industriel | Pipeline complet from scratch | [Synthèse](https://blog.stephane-robert.info/docs/pipeline-cicd/gitlab/fondamentaux/synthese-pipeline/) |

### Bloc 3 — Sécurité (Labs 20–26)

Secrets, scanning, SBOM, branches protégées, durcissement et examen final.

| Lab | Titre | Compétence | Guide lié |
|-----|-------|------------|-----------|
| 20 | Protéger les secrets | Variables protégées, masquage, rotation | [Secrets](https://blog.stephane-robert.info/docs/pipeline-cicd/gitlab/securite/secrets/) |
| 21 | Scanner le code (SAST) | SAST + Secret Detection | [Scanners sécurité](https://blog.stephane-robert.info/docs/pipeline-cicd/gitlab/fondamentaux/securite-scanners/) |
| 22 | Scanner les images | Container Scanning, Trivy | [Supply chain](https://blog.stephane-robert.info/docs/pipeline-cicd/gitlab/securite/supply-chain/) |
| 23 | Scanner les dépendances | Dependency Scanning + SBOM CycloneDX | [Supply chain](https://blog.stephane-robert.info/docs/pipeline-cicd/gitlab/securite/supply-chain/) |
| 24 | Branches protégées | Approval rules, pipeline vert obligatoire | [Branches protégées](https://blog.stephane-robert.info/docs/pipeline-cicd/gitlab/securite/branches-protegees/) |
| 25 | Durcir un pipeline | Épinglage images, least privilege, audit | [Durcissement](https://blog.stephane-robert.info/docs/pipeline-cicd/gitlab/securite/durcissement/) |
| 26 | Examen final | Audit + remédiation d'un pipeline vulnérable | Tous les volets |

## Démarrage rapide (hors labs)

Pour lancer le projet localement sans suivre les labs :

```bash
pip install -r requirements-dev.txt
pytest                          # tests
ruff check app/ tests/          # lint
uvicorn app.main:app --reload   # API sur http://127.0.0.1:8000
```

## Formation complète

Ce dépôt est le support pratique de la formation **GitLab CI/CD** :

- [Formation GitLab CI/CD — Hub](https://blog.stephane-robert.info/docs/pipeline-cicd/gitlab/) — point d'entrée
- [Page des labs](https://blog.stephane-robert.info/docs/pipeline-cicd/gitlab/labs/) — instructions détaillées de chaque lab
- [Concepts de base](https://blog.stephane-robert.info/docs/pipeline-cicd/gitlab/fondamentaux/concepts-base/) — prérequis conseillé avant de commencer

## Contribuer

Les contributions passent par un fork et une merge request. Consultez [CONTRIBUTING.md](./CONTRIBUTING.md) pour les règles de branche, les attentes de validation et les exigences de sécurité.

Pour les changements CI/CD, validez toujours le pipeline avant push :

```bash
glab ci lint .gitlab-ci.yml
```

## Licence

Creative Commons Attribution 4.0 International (CC BY 4.0).

L'attribution de l'auteur d'origine est obligatoire en cas de réutilisation,
de redistribution ou d'adaptation.

Voir [LICENSE](./LICENSE).
