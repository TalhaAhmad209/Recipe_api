# Recipe API

Recipe API is a Django-based RESTful API that allows you to manage recipes. It provides endpoints to create, view, and delete recipes.

## Features

- Create a new recipe with a title, ingredients, and instructions.
- View a list of all recipes.
- View details of a specific recipe.
- Delete a recipe.

## Installation

1. Clone the repository:

```bash
$ git clone https://github.com/TalhaAhmad209/recipe-api.git
$ cd recipe-api
```

2. Set up a virtual environment:

```python
$ python3 -m venv venv
$ source venv/bin/activate
```

3. Install the dependencies:

```python
pip install -r requirements.txt
```

4. Run the migrations:

```python
python manage.py migrate
```

5. Run the migrations:

```python
python manage.py runserver
```

The API will be accessible at http://localhost:8000/api/recipes/.

# Usage
## Create a Recipe

Endpoint: POST /api/recipes/

Create a new recipe by sending a POST request to the above endpoint. The request body should include the following fields:

title (string): The title of the recipe.
ingredients (string): The list of ingredients required for the recipe.
instructions (string): The step-by-step instructions to prepare the recipe.

## Retrieve a List of Recipes

Endpoint: GET /api/recipes/

Retrieve a list of all recipes by sending a GET request to the above endpoint. The response will include an array of recipe objects, each containing the following fields:

id (integer): The unique identifier of the recipe.
title (string): The title of the recipe.
ingredients (string): The list of ingredients required for the recipe.
instructions (string): The step-by-step instructions to prepare the recipe.
created_at (string): The date and time when the recipe was created.

## Retrieve a Specific Recipe

Endpoint: GET /api/recipes/<id>/

Retrieve the details of a specific recipe by sending a GET request to the above endpoint, replacing <id> with the actual recipe ID. The response will include the fields mentioned above.

## Delete a Recipe

Endpoint: DELETE /api/recipes/<id>/delete/

Delete a specific recipe by sending a DELETE request to the above endpoint, replacing <id> with the actual recipe ID. The recipe will be permanently removed from the system.

