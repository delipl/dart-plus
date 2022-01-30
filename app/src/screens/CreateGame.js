import React, { useState, useEffect } from 'react'
import { TouchableOpacity, StyleSheet, View, FlatList } from 'react-native'
import { Text } from 'react-native-paper'
import Background from '../components/Background'
import Header from '../components/Header'
import MHeader from '../components/MidHeader'
import Paragraph from '../components/Paragraph'
import BParagraph from '../components/BigParagraph'
import MSParagraph from '../components/MSParagraph'
import SParagraph from '../components/SmallParagraph'
import SHeader from '../components/SmallHeader'
import MParagraph from '../components/MidParagraph'
import MRedParagraph from '../components/MidRedParagraph'
import Button from '../components/Button'
import TextInput from '../components/TextInput'
import BackButton from '../components/BackButton'
import { theme } from '../core/theme'
import {
  Switch,
  Colors,
  TouchableRipple,
  useTheme,
  Appbar,
} from 'react-native-paper';

export default function LoginScreen({ navigation }) {
    const [data, setData] = useState([])
    const [valueNormal, setNormalValue] = useState(true);
    const [doubleIn, setdoubleIn] = useState(false);
    const [doubleOut, setdoubleOut] = useState(false);

    const switchDoubleInlLabel = `switch ${
      doubleIn === true ? 'on' : 'off'
    }`;

    const switchDoubleOutlLabel = `switch ${
      doubleOut === true ? 'on' : 'off'
    }`;

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
          <View style={styles.row}>

          <View style={styles.screen}>
    </View>
        </View>
          <View style={{
            flexDirection: "row", padding:10,
            }}> 
            <MSParagraph>Double In      </MSParagraph>
            <Switch
              style={{ width: 20, height: 22
                }}
              value={doubleIn}
              onValueChange={() => setdoubleIn(!doubleIn)}
              color={theme.colors.primary}
            />
          </View>
          <View style={{
            flexDirection: "row"
            }}> 
            <MSParagraph>Double Out   </MSParagraph>
            <Switch
              style={{ width: 20, height: 22
                }}
              value={doubleOut}
              onValueChange={() => setdoubleIn(!doubleOut)}
              color={theme.colors.primary}
            />
          </View>
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
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: Colors.grey200,
    padding: 4,
  },

  row: {
    justifyContent: 'center',
    alignItems: 'center',
  },

  fab: {
    margin: 8,
  },
});
