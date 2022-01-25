import React from 'react'
import { StyleSheet } from 'react-native'
import { Text } from 'react-native-paper'
import { theme } from '../core/theme'

export default function Header(props) {
  return <Text style={styles.header} {...props} />
}

const styles = StyleSheet.create({
  header: {
    fontSize: 12,
    color: theme.colors.primary,
    fontWeight: 'bold',
    textAlign: 'right',
    marginBottom: 6,
    marginTop: 6,
  },
})
