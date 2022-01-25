import React, { useState, useEffect } from 'react'
import { TouchableOpacity, StyleSheet, View, FlatList } from 'react-native'
import { Text } from 'react-native-paper'
import Background from '../components/Background'
import Header from '../components/Header'
import MHeader from '../components/MidHeader'
import Paragraph from '../components/Paragraph'
import BParagraph from '../components/BigParagraph'
import SParagraph from '../components/SmallParagraph'
import SHeader from '../components/SmallHeader'
import MParagraph from '../components/MidParagraph'
import MRedParagraph from '../components/MidRedParagraph'
import Button from '../components/Button'
import TextInput from '../components/TextInput'
import BackButton from '../components/BackButton'
import { theme } from '../core/theme'


export default function LoginScreen({ navigation }) {
    const [doubleIn, setdoubleIn] = useState(true);
    const [data, setData] = useState([])
    
    return (
        <View
        style={{
          flexDirection: "row"
          }}>
          <BackButton goBack={navigation.goBack} />
        <View style={{flex: 1, 
          alignSelf: 'center',
          alignItems: 'center',
          justifyContent: 'center',
          marginTop: 120}}> 
          
          <MHeader>
            #91238
          </MHeader>
        
          <Header>
            siema 3
          </Header>
        </View>
  
        <View style={{flex: 1, alignSelf: 'center',
      alignItems: 'center',
      justifyContent: 'center',}}>
          <Header>Lista graczy: </Header>
        <Paragraph>
          <FlatList
              data={data.players}
              keyExtractor={({ id }, index) => id}
              renderItem={({ item }) => (
                <View style={{flexDirection: "row",flexWrap: "wrap", marginRight: 10}}>
                  <SParagraph>{item.nick} </SParagraph>
                  <SHeader>{item.points}</SHeader>
                </View>
              )}
            />
          </Paragraph>
        </View>
      </View>
    )
}

