import React, { useEffect, useState} from 'react';
import { ActivityIndicator, FlatList, Text, View } from 'react-native';
import Background from '../components/Background'
import Logo from '../components/Logo'
import DartLogo from '../components/DartLogo'
import Header from '../components/Header'
import BHeader from '../components/BigHeader'
import Paragraph from '../components/Paragraph'
import BParagraph from '../components/BigParagraph'
import MParagraph from '../components/MidParagraph'
import MRedParagraph from '../components/MidRedParagraph'
import Button from '../components/Button'
import { io } from "socket.io-client";

const ENDPOINT = "http://192.168.192.3:8000";

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
  var socket = io(ENDPOINT);
  
  useEffect(() => {
    console.log("Connect:")

    socket.on('user_activated', (data) => {
       setData(data)
    })

  }, []);

  if (data.length === 0) return <div>Loading...</div>

  return (
    <Background>
      <BHeader>
        {data.points}
      </BHeader>
      <BParagraph>
        {data.nick}
      </BParagraph>
      <Header>
      <Images attempts={data.attempts}/>
      </Header>
      <Paragraph>
      {/* <FlatList
          data={data.players}
          keyExtractor={({ id }, index) => id}
          renderItem={({ item }) => (
            <Paragraph>{item.nick} - {item.points} </Paragraph>
          )}
        /> */}
      </Paragraph>
    </Background>
  );
}
