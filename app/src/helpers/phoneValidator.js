export function phoneValidator(phone) {
  if (!phone) return "Phone can't be empty."
  if (!/^\d+$/.test(phone)) return "Enter only numbers"
  if (phone.length < 9) return 'Number has 9 numbers'
  return ''
}


