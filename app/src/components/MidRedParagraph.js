import React from 'react'
import { StyleSheet } from 'react-native'
import { Text } from 'react-native-paper'
import { theme } from '../core/theme'


export default function Paragraph(props) {
  return <Text style={styles.text} {...props} />
}

const styles = StyleSheet.create({
  text: {
    fontSize: 35,
    lineHeight: 21,
    color: theme.colors.primary,
    textAlign: 'center',
    marginBottom: 22,
    marginTop: 22,
  },
})
