# Concours Pull de Noël 🎄

Petite app web Flask pour organiser un concours de pulls de Noël avec QR codes individuels.

Chaque pull a un identifiant unique. Un QR code collé sur le pull renvoie vers sa page de vote.

## Fonctionnalités

- 50 pulls pré-générés (facilement modifiables dans `static/pulls.json`)
- Page individuelle par pull + bouton de vote
- Classement en temps réel
- QR codes générables à la demande

## Déploiement gratuit sur Render (recommandé)

### 1. Pousser sur GitHub

1. Crée un nouveau repository sur GitHub
2. Clone-le en local
3. Copie tout le contenu de ce dossier dans le repo
4. Commit et push :

```bash
git add .
git commit -m "Initial commit - Concours Pull de Noël"
git push
```

### 2. Déployer sur Render

1. Va sur [render.com](https://render.com) et crée un compte (gratuit)
2. **New → Web Service**
3. Connecte ton repository GitHub
4. Configure :
   - **Name** : `pull-noel` (ou ce que tu veux)
   - **Region** : Frankfurt (ou le plus proche)
   - **Branch** : `main`
   - **Runtime** : Python 3
   - **Build Command** : `pip install -r requirements.txt`
   - **Start Command** : `gunicorn app:app`
   - **Instance Type** : **Free**
5. Clique sur **Create Web Service**

Render te donnera une URL du type : `https://pull-noel.onrender.com`

### 3. Générer les vrais QR codes

Une fois l'app déployée, récupère l'URL finale et lance :

```bash
python generate_qrs.py https://pull-noel.onrender.com
```

Les QR codes dans le dossier `qrcodes/` seront régénérés avec la bonne URL.  
Tu peux ensuite les imprimer / les coller sur les pulls.

> **Note importante** : Sur le plan gratuit de Render, le filesystem est éphémère.  
> Les votes sont stockés dans `static/pulls.json`. Ils peuvent se réinitialiser si le service redémarre (après 15 min d'inactivité ou lors d'un nouveau déploiement).  
> Pour un événement de quelques heures, c'est généralement suffisant. Pense à noter les résultats à la fin.

## Lancer en local

```bash
pip install -r requirements.txt
python app.py
```

Ouvre http://localhost:5000

Pour générer les QR en local :

```bash
python generate_qrs.py http://localhost:5000
```

## Structure

```
.
├── app.py                 # Application Flask
├── generate_qrs.py        # Générateur de QR codes
├── requirements.txt
├── static/
│   └── pulls.json         # Données des pulls + votes
├── templates/
│   ├── leaderboard.html
│   └── pull.html
└── qrcodes/               # QR codes générés
```

## Personnalisation

Édite `static/pulls.json` pour changer les noms, propriétaires et descriptions des pulls.

Bon concours !
