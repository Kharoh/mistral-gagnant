import * as React from 'react';
import CssBaseline from '@mui/material/CssBaseline';
import Divider from '@mui/material/Divider';
import AppAppBar from './components/AppAppBar';
import Hero from './components/Hero';
import LogoCollection from './components/LogoCollection';
import Highlights from './components/Highlights';
import Pricing from './components/Pricing';
import Features from './components/Features';
import Testimonials from './components/Testimonials';
import FAQ from './components/FAQ';
import Footer from './components/Footer';
import AppTheme from '../shared-theme/AppTheme';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';

export default function MarketingPage(props) {

  const [currentMessage, setCurrentMessage] = React.useState("");
  const [pastMessages, setPastMessages] = React.useState(["Bonjour ! Je suis votre assistant virtuel de mode. Comment puis-je vous aider aujourd'hui ?"])
  const [username, setUsername] = React.useState("");

  const sendMessage = () => {
    // update first time past messages
    setPastMessages([currentMessage, ...pastMessages])
    // clear input field
    setCurrentMessage("")
    // send message to server localhost:5000/chat as user_input and retrieve the response with http post
    fetch('http://localhost:5000/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        user_input: currentMessage,
        thread_id: username,
      }),
      timeout: 1000,
    })
    .then(response => response.json())
    .then(data => {
      // update state with response from server
      setPastMessages([data.response, currentMessage, ...pastMessages])
      // Il faut remettre le current message car le fetch wrap le state sans le current message...
    })
    .catch(error => console.error('Error:', error));
  }

  return (
    <AppTheme {...props}>
      <CssBaseline enableColorScheme />
      <AppAppBar />
      <Box 
      id="messages"
      sx={(theme) => ({
        width: '100%',
        backgroundRepeat: 'no-repeat',

        backgroundImage:
          'radial-gradient(ellipse 80% 50% at 50% -20%, hsl(210, 100%, 90%), transparent)',
        ...theme.applyStyles('dark', {
          backgroundImage:
            'radial-gradient(ellipse 80% 50% at 50% -20%, hsl(210, 100%, 16%), transparent)',
        }),
        height:'70vh',
        paddingTop: '20vh',
        marginBottom: '5vh',
        overflowY: 'scroll',
        flexDirection: 'column-reverse',
        display: 'flex',
        alignItems: 'center',
      })}>
        {pastMessages.map((message, index) => {
          return <Typography 
          
          sx={{
            textAlign: 'left',
            color: 'text.secondary',
            width: { sm: '50%', md: '50%' },
            alignSelf: { sm: 'center', md: 'center' },
            justifySelf: { sm: 'center', md: 'center'},
            marginTop: { sm: '10px', md: '10px'},
          }}
          
          key={index}>
            <Typography sx={{color: 'text.primary'}}>
             {index % 2 === 0 ? "Assistant: " : (username || "Utilisateur") + ": " } 
            </Typography>
             {message}
          </Typography>
        })}
      </Box>
      <Hero 
        pastMessages={pastMessages} 
        setPastMessages={setPastMessages} 
        currentMessage={currentMessage}
        setCurrentMessage={setCurrentMessage}
        username={username}
        setUsername={setUsername}
        sendMessage={sendMessage}
      />
      <div>
        <LogoCollection />
        {/* <Features />
        <Divider />
        <Testimonials />
        <Divider />
        <Highlights />
        <Divider />
        <Pricing />
        <Divider />
        <FAQ />
        <Divider /> */}
        <Footer />
      </div>
    </AppTheme>
  );
}
