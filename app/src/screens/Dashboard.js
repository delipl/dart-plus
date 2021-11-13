import React, { useEffect, useState} from 'react';
import { ActivityIndicator, FlatList, Text, View } from 'react-native';
import Background from '../components/Background'
import Logo from '../components/Logo'
import DartLogo from '../components/DartLogo'
import Header from '../components/Header'
import BHeader from '../components/BigHeader'
import Paragraph from '../components/Paragraph'
import BParagraph from '../components/BigParagraph'
import Button from '../components/Button'

function Images(props) {
  const k = props.attempts
  let render = []
  for (let i = 0; i < k; i++) {
    render.push(<DartLogo></DartLogo>)
  }
  return render
}

export default function Dashboard({ navigation }){
  const [isLoading, setLoading] = useState(true);
  const [data, setData] = useState([]);

  const getGame = async () => {
     try {
      const response = await fetch('http://192.168.192.3:8000/info', {
        method: 'GET',
        headers: {
          Accept: 'application/json',    
          'Content-Type': 'application/json'
        }
      });
      const json = await response.json();
      setData(json);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  }
  useEffect(() => {
    getGame();
  }, []);

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
