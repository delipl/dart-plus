import React from 'react'
import { StyleSheet } from 'react-native'
import { Text } from 'react-native-paper'

export default function Paragraph(props) {
  return <Text style={styles.text} {...props} />
}

const styles = StyleSheet.create({
  text: {
    fontSize: 76,
    lineHeight: 21,
    textAlign: 'center',
    marginBottom: 42,
    marginTop: 42,
  },
})
