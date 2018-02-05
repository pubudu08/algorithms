import {Ingredient} from '../shared/ingredient.model';

export class ShoppingListService {
  private _ingredients: Ingredient[] = [
    new Ingredient('Apples', 5),
    new Ingredient('Tomatoes', 10),
  ];


  get ingredients(): Ingredient[] {
    return this._ingredients;
  }

  addIngredient(ingredient: Ingredient) {
    this._ingredients.push(ingredient);

  }
}
