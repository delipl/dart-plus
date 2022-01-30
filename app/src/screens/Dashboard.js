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
import { Base64 } from 'js-base64';


export default function Dashboard({ navigation }) {
  const [status, setStatus] = useState({ value: '', error: '' })
  const [isLoading, setLoading] = useState(true);
  const [data, setData] = useState([]);

  const onGamePressed = () => {
    var headers = new Headers();
    headers.set('Authorization', 'Basic ' + Base64.encode(localStorage.getItem('token') + ":"));

    const requestOptions = {
      method: 'GET',
      headers: headers
    };

    try {fetch(global.GAME_CHECK, requestOptions)
      .then(response => response.json())
      .then(json => {
        console.log(json);
        if (json.message){
          setData(json)
          console.log(json);
        }
      });
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
  }

  const onLogoutPress = () => {
    localStorage.removeItem("token");
    navigation.navigate('StartScreen2');
  };

  if (!isLoading) {
    if (data.id == 0) {
      console.log("Gra NIE istnieje: ")
      console.log(data)
      setPhone({ ...phone, error: data.message })
      setData(1)
      setLoading(true)
    } else if (data.id > 0) {
      console.log("Gra istnieje: ")
      console.log(data)
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
      <Button mode="contained" onPress={onGamePressed}>Game</Button>      
      <Button mode="outlined"onPress={onLogoutPress}>Logout</Button>
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
