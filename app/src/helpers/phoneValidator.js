export function phoneValidator(phone) {
  if (!phone) return "Phone can't be empty"
  if (!/^\d+$/.test(phone)) return "Enter numbers only"
  if (phone.length < 9) return 'Number has 9 numbers'
  return ''
}


