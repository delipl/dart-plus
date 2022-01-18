import React, { useRef, useEffect, useState} from 'react';
import { AppState, ActivityIndicator, FlatList, Text, View } from 'react-native';
import Background from '../components/Background'
import Logo from '../components/Logo'
import DartLogo from '../components/DartLogo'
import Header from '../components/Header'
import BHeader from '../components/BigHeader'
import Paragraph from '../components/Paragraph'
import BParagraph from '../components/BigParagraph'
import SParagraph from '../components/SmallParagraph'
import SHeader from '../components/SmallHeader'
import MParagraph from '../components/MidParagraph'
import MRedParagraph from '../components/MidRedParagraph'
import Button from '../components/Button'
import { io } from "socket.io-client";
import '../helpers/global.js'
import { theme } from '../core/theme'

function Images(props) {
  const k = props.attempts
  let render = []
  for (let i = 0; i < k; i++) {
    render.push(<DartLogo></DartLogo>)
  }
  return render
}



export default function Dashboard({ navigation }){
  const [data, setData] = useState([])
  
  useEffect(() => {
    const socket = io(global.IP);

    socket.on(global.PHONE, (data) => {
      setData(data)
    })
    socket.emit("test", global.PHONE)
  }, []);

  if (data.length === 0) return <div>Loading...</div>

  return (
    <View
      style={{
        flexDirection: "row",
        paddingTop: 115
      }}>
      <View style={{flex: 4, alignSelf: 'center',
    alignItems: 'center',
    justifyContent: 'center'}}> 
        
        <BHeader>
          {data.points}
        </BHeader>
        <BParagraph>
          {data.nick}
        </BParagraph>
        <Header>
        <Images attempts={data.attempts}/>
        </Header>
      </View>

      <View style={{flex: 1, alignSelf: 'center',
    alignItems: 'center',
    justifyContent: 'center',}}>
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
    
  );
}
