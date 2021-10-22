import React from "react";
import logo from './logo.png'; 

import {
  StyleSheet,
  SafeAreaView,
  View,
  Text,
  TouchableOpacity,
  TextInput,
  Image,
} from "react-native";
import { StatusBar } from "expo-status-bar";
import { FontAwesome5 } from "@expo/vector-icons";
import Constants from "expo-constants";



export default function MomoLogin() {
  return (
    <SafeAreaView style={styles.container}>
      {/* https://docs.expo.io/versions/latest/sdk/status-bar */}
      <StatusBar style="light" />        

      <View style={styles.content}>
        <View style={styles.logoContainer}>
        <Text style={styles.logoText}>DartPlus</Text>
        <Image
                style={styles.img}                      
                source={logo}
                
            />
 
      </View>
        <View style={styles.textWrapper}>

          <Text style={styles.userText}></Text>
        </View>

        <View style={styles.form}>
          {/* https://docs.expo.io/guides/icons */}
          <FontAwesome5 name="address-book" style={styles.iconLock} />

          {/* https://reactnative.dev/docs/textinput */}
          <TextInput
            style={styles.inputPassword}
            keyboardType="alfanumeric"
            secureTextEntry={false}
            autoFocus={true}
            placeholder="Name"
            placeholderTextColor="#929292"
          />

          {/* https://reactnative.dev/docs/touchableopacity */}
          <TouchableOpacity style={styles.buttonLogin}>
            <Text style={styles.buttonLoginText}>Add</Text>
          </TouchableOpacity>
        </View>

        <View style={styles.action}>
          <TouchableOpacity>
            <Text style={styles.userText}>Powered by chłopaki od Emilki</Text>
          </TouchableOpacity>
        </View>
      </View>
    </SafeAreaView>
  );
}

const TEXT = {
  color: "#fff",
  textAlign: "center",
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#A8DF6A",
    paddingTop: Constants.statusBarHeight,
  },
  content: {
    paddingHorizontal: 30,
  },
  textWrapper: {
    marginTop: 60,
    marginBottom: 30,
  },
  logoText: {
    ...TEXT,
    fontSize: 35,
    lineHeight: 50,
    fontWeight: "bold",
    color: "#121A65",
    position: 'absolute',
    alignSelf: 'center',
    bottom: '50%'

  },
  img: {
    width: 50,
    height: 50,
      position: 'absolute',
      alignSelf: 'center',
      bottom: '5%',
      left: '68%',
      
    },
  userText: {
    ...TEXT,
    fontSize: 12,
    lineHeight: 1100,
    left: 200,
    
    
  },
  form: {
    marginBottom: 30,
  },
  iconLock: {
    color: "#121A65",
    position: "absolute",
    fontSize: 16,
    top: 22,
    left: 22,
    zIndex: 10,
  },
  inputPassword: {
    height: 60,
    borderRadius: 30,
    paddingHorizontal: 30,
    fontSize: 20,
    color: "#121A65",
    backgroundColor: "#fff",
    textAlign: "center",
    textAlignVertical: "center",
  },
  buttonLogin: {
    height: 50,
    borderRadius: 25,
    backgroundColor: "#121A65",
    justifyContent: "center",
    marginTop: 15,
  },
  buttonLoginText: {
    ...TEXT,
  },
  action: {
    flexDirection: "row",
    justifyContent: "center",
  },
  logoContainer: {
    // flex:1,
    // paddingTop:100,
    // flexDirection: 'row',
    position: 'absolute',
        marginTop: 80,
        left: 0,
        right: 0,
  },
  
});