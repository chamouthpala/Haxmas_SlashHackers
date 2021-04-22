import React from 'react';
import {View, StyleSheet, Text, Image} from 'react-native';
import { ScrollView } from 'react-native-gesture-handler';
import YoutubePlayer from 'react-native-youtube-iframe';
const tuteTwo = () => {
  return (
      <ScrollView>
    <View>
        <Image
  source={require('../../assets/logo.jpeg')}
    style={styles.image} />
    
         <Text style={[styles.title1,styles.setColorB,styles.setFontSize]}>
      MY VOCAL BUDDY 
      </Text> 
      <Text style={[styles.title,styles.setColorB,styles.setFontSize]}>
      Tutorial 2
      </Text> 

      <View>
      <YoutubePlayer
        height={300}
        play={true}
        videoId={'Po-WMo8vXRY'}
      />
      <YoutubePlayer
        height={300}
        play={true}
        videoId={'iWn1CkIU_rc'}
      />
      <YoutubePlayer
        height={300}
        play={true}
        videoId={'d7TPbJ6Dtd0'}
      />
     </View>
    </View>
    </ScrollView>
  );

  }
const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    backgroundColor: "#00004d",
    marginHorizontal: 16,
    alignItems: "center",
    justifyContent: "center",
},
title: {
    textAlign: 'center',
    marginVertical: 8,
    marginBottom: 30,
},
title1: {
    textAlign: 'center',
    marginVertical: 8,
   
},
fixToText: {
    flexDirection: 'row',
    justifyContent: 'space-between',
},
separator: {
    marginVertical: 8,
    borderBottomColor: '#737373',
    borderBottomWidth: StyleSheet.hairlineWidth,
},
image: {
    // marginBottom: 20,
    marginLeft: 90,
     width: 200,
    height: 200, 
    borderRadius: 100,
  },
setColorLBlue: {
    color: '#1FFBEE'
},
setColorWhite: {
    color: '#ffffff'
},
setFontSize: {
    fontSize: 30,
    fontWeight: 'bold'
},
});

export default tuteTwo;