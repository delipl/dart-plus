import { DefaultTheme } from 'react-native-paper'

export const theme = {
  ...DefaultTheme,
  colors: {
    ...DefaultTheme.colors,
    text: '#000000',
    primary: '#a70c25',
    secondary: '#414757',
    error: '#f13a59',
  },
  container: {
    backgroundColor: "#7CA1B4",
    flex: 1,
  },
  goldContainer: {
    flex: 2,
    backgroundColor: 'gold',
  },
  redContainer: {
    flex: 1,
    backgroundColor: 'red',
  },
}
