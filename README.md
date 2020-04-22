# Password Manager

A minimalistic Django App for storing encrypted accounts in the cloud.

You can find the related front-end application [here](https://github.com/janos-gonye/pass-manager-frontend).

## Setup for development
0. Clone the project.
```sh
git clone https://github.com/janos-gonye/pass-manager.git
cd ./pass-manager
```
1. Create the `.env` file by coping the template file.
```sh
cp ./.env.template ./.env
```
2. Set your environment variables.
3. Install `docker` and `docker-compose` if they are not installed yet.
4. Run docker-compose.
```sh
docker-compose up --build
```
5. The app is running on http://localhost:8000.

---
Thanks for reading,  
Johnny
