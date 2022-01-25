import React, { useState, useEffect } from 'react'
import { TouchableOpacity, StyleSheet, View } from 'react-native'
import { Text } from 'react-native-paper'
import Background from '../components/Background'
import Logo from '../components/Logo'
import Header from '../components/Header'
import Button from '../components/Button'
import TextInput from '../components/TextInput'
import BackButton from '../components/BackButton'
import { theme } from '../core/theme'
import { phoneValidator } from '../helpers/phoneValidator'
import { getBoardId } from '../helpers/getBoardId'
import { passwordValidator } from '../helpers/passwordValidator'
import { encrypt_password } from '../helpers/encyption'
import '../helpers/global.js'
import BParagraph from '../components/BigParagraph'


export default function Dashboard({ navigation }) {
  const [status, setStatus] = useState({ value: '', error: '' })
  const [isLoading, setLoading] = useState(true);
  const [data, setData] = useState([]);

  const onGamePressed = () => {
    // Are you in game ? 
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ phone: global.PHONE})
    };

    try {fetch(global.GAME_CHECK, requestOptions)
      .then(response => response.json())
      .then(json => {
        if (json.message){
          setData(json)
        }
      });
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
  }

  if (!isLoading) {
    if (data.status == 1) {
      console.log(data.message)
      setPhone({ ...phone, error: data.message })
      setData(1)
      setLoading(true)
    }
    if (data.status == 0) {
      console.log(data.message)
      setLoading(true)
      navigation.reset({
        index: 0,
        routes: [{ name: 'Dashboard' }],
      })
    }
  }

  return (
    <Background>
      <Header>Dart-Plus.APP</Header>
      <Button mode="contained"onPress={() => navigation.navigate('LoginScreen')}>Profile</Button>      
      <Button mode="contained"onPress={onGamePressed}>Game</Button>      
      <Button mode="outlined"onPress={() => navigation.navigate('RegisterScreen')}>Logout</Button>
    </Background>
  )
}
  const styles = StyleSheet.create({
    forgotPassword: {
      width: '100%',
      alignItems: 'flex-end',
      marginBottom: 24,
    },
    row: {
      flexDirection: 'row',
      marginTop: 4,
    },
    forgot: {
      fontSize: 13,
      color: theme.colors.secondary,
    },
    link: {
      fontWeight: 'bold',
      color: theme.colors.primary,
    },
})
