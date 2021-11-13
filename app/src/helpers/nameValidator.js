export function nameValidator(name) {
  if (!name) return "Name can't be empty."
  if (name.lengh > 20 || name.lengh < 3) return 'Name format is not accepted!'
  return ''
}
