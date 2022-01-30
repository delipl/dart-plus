import React, { useState, useEffect } from 'react'
import { Provider } from 'react-native-paper'
import { NavigationContainer } from '@react-navigation/native'
import { createStackNavigator } from '@react-navigation/stack'
import { theme } from './src/core/theme'
import useToken from './src/components/useToken'
import Header from './src/components//Header'
import Header2 from './src/components/Header2'

import {
  StartScreen,
  LoginScreen,
  RegisterScreen,
  ResetPasswordScreen,
  Dashboard,
  Game,
  CreateGame,
} from './src/screens'

const Stack = createStackNavigator()


export default function App() {
  const { token, removeToken, setToken } = useToken();
  const [screenName, setScreenName] = useState({value:''});


  useEffect(() => {
    if (!token && token!=="") {
      console.log("nie mam");
      screenName.value = "StartScreen"
    } else {
      console.log("mam");
      screenName.value = "Dashboard"
      
    }
  
  }, [])

  return (
    <Provider theme={theme}>
        <NavigationContainer >
          <Stack.Navigator screenOptions={{
            headerShown: false,
          }}>
          {token == null ? (
            <Stack.Screen name="StartScreen" component={StartScreen} />

          ) : (
            // User is signed in
            <Stack.Screen name="Dashboard" component={Dashboard} />
            )}
          <Stack.Screen name="LoginScreen" component={LoginScreen} />
          <Stack.Screen name="RegisterScreen" component={RegisterScreen} />
          <Stack.Screen name="Game" component={Game} />
          <Stack.Screen name="CreateGame" component={CreateGame} />
          <Stack.Screen name="ResetPasswordScreen" component={ResetPasswordScreen}/>
          <Stack.Screen name="StartScreen2" component={StartScreen} />
          <Stack.Screen name="Dashboard2" component={Dashboard} />
        </Stack.Navigator>
        
      </NavigationContainer>
    </Provider>
  )
}
