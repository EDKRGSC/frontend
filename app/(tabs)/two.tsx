import React from 'react';
import { StyleSheet, TouchableOpacity} from 'react-native';

import EditScreenInfo from '@/components/EditScreenInfo';
import { Text, View } from '@/components/Themed';
import styled from 'styled-components/native';

type Props = {
  text: string;
}

// const CustomButton: React.FC<Props> = ({ text }: Props) => {
//   return (
//     <TouchableOpacity>
//         <View>
//             <Text>{text}</Text>
//         </View>
//     </TouchableOpacity>
//   )
// }
// const ButtonCont = styled.View`
//     flex: 1;
// `

export default function TabTwoScreen() {
  return (
      <TouchableOpacity>
        <Container>
          <H1 >Report</H1>
          <Text >y</Text>
          <Row/>
        </Container>
      </TouchableOpacity>
    
  );
}

const Container = styled.View`
    flex: 1;
    align-Items: center;
    justify-Content: center;
    background-color: #5C677D;
`

const H1 = styled.Text`
    font-Size: 20px;
    color: rgba(218, 22, 22, 1);
    font-Weight: bold;
`

const Row = styled.View`

`