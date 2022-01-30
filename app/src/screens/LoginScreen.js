import React, { useState, useEffect } from 'react'
import { TouchableOpacity, StyleSheet, View } from 'react-native'
import { Text } from 'react-native-paper'
import Background from '../components/Background'
import Logo from '../components/Logo'
import Header from '../components/Header'
import Button from '../components/Button'
import TextInput from '../components/TextInput'
import { Base64 } from 'js-base64';
import BackButton from '../components/BackButton'
import { theme } from '../core/theme'
import { phoneValidator } from '../helpers/phoneValidator'
import { getBoardId } from '../helpers/getBoardId'
import { passwordValidator } from '../helpers/passwordValidator'
import { encrypt_password } from '../helpers/encyption'
import useToken from '../components/useToken'
import '../helpers/global.js'
import axios from "axios";

export default function LoginScreen({ navigation }) {
  const [phone, setPhone] = useState({ value: '', error: '' })
  const [password, setPassword] = useState({ value: '', error: '' })
  const [isLoading, setLoading] = useState(true);
  const [data, setData] = useState([]);

  global.BOARDID = getBoardId(window.location.href)

  function onLoginPressed(event) {
    var headers = new Headers();
    console.log(phone.value)
    console.log(password.value)
    headers.set('Authorization', 'Basic ' + Base64.encode(phone.value + ":" + password.value));

    fetch(global.LOGIN, {method:'GET',
        headers: headers,
       })
    .then(response => response.json())
    .then(json => {
      setData(json)
      localStorage.setItem('token', json.token);
      setLoading(false);
    });
  }

  if (!isLoading) {
    if (data.status == 0) {
      console.log(data.message)
      setPhone({ ...phone, error: data.message })
      setData(1)
      setLoading(true)
    }
    if (data.status == 1) {
      console.log(data.message)
      setLoading(true)
      global.PHONE = String(phone.value)
      if (global.BOARDID != 0){
        navigation.reset({
          index: 0,
          routes: [{ name: 'Game' }],
        })
      } else {
        navigation.navigate('Dashboard2');
      }
    }
  }

  return (
    <Background>
      <BackButton goBack={navigation.goBack} />
      {/* <Logo /> */}
      <Header>Let's play dart game!</Header>
      <TextInput
        label="Phone"
        returnKeyType="next"
        value={phone.value}
        onChangeText={(text) => setPhone({ value: text, error: '' })}
        error={!!phone.error}
        errorText={phone.error}
        autoCapitalize="none"
        autoCompleteType="phone"
        textContentType="phoneAddress"
        keyboardType="phone-address"
        keyboardType="numeric"
        maxLength={9}
      />
      <TextInput
        label="Password"
        returnKeyType="done"
        value={password.value}
        onChangeText={(text) => setPassword({ value: text, error: '' })}
        error={!!password.error}
        errorText={password.error}
        secureTextEntry
      />
      <View style={styles.forgotPassword}>
        <TouchableOpacity
          onPress={() => navigation.navigate('ResetPasswordScreen')}
        >
          <Text style={styles.forgot}>Forgot your password?</Text>
        </TouchableOpacity>
      </View>
      <Button mode="contained" onPress={onLoginPressed}>
        Login
      </Button>
      <View style={styles.row}>
        <Text>Don’t have an account? </Text>
        <TouchableOpacity onPress={() => navigation.replace('RegisterScreen')}>
          <Text style={styles.link}>Sign up</Text>
        </TouchableOpacity>
      </View>
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
