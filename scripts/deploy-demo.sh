#!/bin/sh
# Script de déploiement de démonstration
# En production, ce script serait remplacé par un vrai déploiement (Ansible, kubectl, etc.)
set -eu

ENVIRONMENT="${1:?Usage: deploy-demo.sh <environment>}"

echo "=== Déploiement de démonstration ==="
echo "Environnement : $ENVIRONMENT"
echo "Commit        : ${CI_COMMIT_SHORT_SHA:-local}"
echo "Date          : $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo ""
echo "En environnement réel, ce script :"
echo "  1. Tirerait l'image depuis le registre"
echo "  2. Arrêterait le conteneur précédent"
echo "  3. Lancerait le nouveau conteneur"
echo "  4. Vérifierait le health check"
echo ""
echo "=== Déploiement simulé avec succès ($ENVIRONMENT) ==="
