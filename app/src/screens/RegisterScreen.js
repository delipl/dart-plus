import React, { useEffect, useState } from 'react'
import { View, StyleSheet, TouchableOpacity, ActivityIndicator, FlatList } from 'react-native'
import { Text } from 'react-native-paper'
import Background from '../components/Background'
import Logo from '../components/Logo'
import Header from '../components/Header'
import Button from '../components/Button'
import TextInput from '../components/TextInput'
import BackButton from '../components/BackButton'
import { theme } from '../core/theme'
import { phoneValidator } from '../helpers/phoneValidator'
import { encrypt_password } from '../helpers/encyption'
import { passwordValidator } from '../helpers/passwordValidator'
import { nameValidator } from '../helpers/nameValidator'
import { cos } from 'react-native-reanimated'
import '../helpers/global.js'

export default function RegisterScreen({ navigation }) {
  const [name, setName] = useState({ value: '', error: '' })
  const [phone, setPhone] = useState({ value: '', error: '' })
  const [password, setPassword] = useState({ value: '', error: '' })
  const [isLoading, setLoading] = useState(true);
  const [data, setData] = useState([]);


  const onSignUpPressed = () => {
    var nameError = nameValidator(name.value)
    const phoneError = phoneValidator(phone.value)
    const passwordError = passwordValidator(password.value)
    if (phoneError || passwordError || nameError) {
      setName({ ...name, error: nameError })
      setPhone({ ...phone, error: phoneError })
      setPassword({ ...password, error: passwordError })
      return
    }
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name: name.value, phone: phone.value, password: password.value })
    };

    try {fetch(global.REGISTER, requestOptions)
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
    
  };

  if (!isLoading) {
    if (data.status == 0) {
      console.log(data.message)
      setName({ ...name, error: data.message })
      setData(1)
      setLoading(true)
    }
    if (data.status == 1) {
      console.log(data.message)
      setLoading(true)
      navigation.reset({
        index: 0,
        routes: [{ name: 'LoginScreen' }],
      })
    }
  }
  return (
    <Background>
      <BackButton goBack={navigation.goBack} />
      {/* <Logo /> */}
      <Header>Create Account</Header>
      <TextInput
        label="Name"
        returnKeyType="next"
        value={name.value}
        onChangeText={(text) => setName({ value: text, error: '' })}
        error={!!name.error}
        errorText={name.error}
      />
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
      <Button
        mode="contained"
        onPress={onSignUpPressed}
        style={{ marginTop: 24 }}
      >
        Sign Up
      </Button>
      <View style={styles.row}>
        <Text>Already have an account? </Text>
        <TouchableOpacity onPress={() => navigation.replace('LoginScreen')}>
          <Text style={styles.link}>Login</Text>
        </TouchableOpacity>
      </View>
    </Background>
  )
}

const styles = StyleSheet.create({
  row: {
    flexDirection: 'row',
    marginTop: 4,
  },
  link: {
    fontWeight: 'bold',
    color: theme.colors.primary,
  },
})
