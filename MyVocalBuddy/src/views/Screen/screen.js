// class App extends React.Component {
//     videoBuffer = (isBuffer) =>{
//     console.log(isBuffer)
//     //here you could set the isBuffer value to the state and then do something with it
//     //such as show a loading icon
//     }
//     render() {
//     return (
//     <View style={{ alignItems: 'center', flex: 1, justifyContent: 'center' }}>
//     <Text>My video project!</Text>
//     <View>
//     <Video
//     source={{ uri: 'https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-mp4-file.mp4?_=1' }}
//     style={{ width: 300, height: 300 }}
//     controls={true}
//     onBuffer={this.videoBuffer}
//     ref={(ref) => {
//     this.player = ref
//     }} />
//     </View>
//     </View>
//     )
//     }
//     }