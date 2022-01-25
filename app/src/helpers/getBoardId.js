export function getBoardId(url) {
  var index_get = url.indexOf('?board_id=')
  if (index_get == -1) return ''
  var index_com = url.indexOf('=')
  if (index_com == -1) return ''
  return url.substring(index_com + 1, url.lenght)
}
