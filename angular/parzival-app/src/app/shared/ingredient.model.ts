export class Ingredient {
  // TS has a shortcut feature to assign values to global vars
  // It is a convenient and behind the scene TS will assign values
  // to defined properties below
  constructor(public name: string, public amount: number) {}
}
