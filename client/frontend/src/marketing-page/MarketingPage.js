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
import { io } from "socket.io-client";
import ProductShowcase from './components/ProductShowcase';


export default function MarketingPage(props) {

  const [currentMessage, setCurrentMessage] = React.useState("");
  const [pastMessages, setPastMessages] = React.useState(["Bonjour ! Je suis votre assistant virtuel de mode. Comment puis-je vous aider aujourd'hui ?"])
  const [username, setUsername] = React.useState("");

  const SOCKET_SERVER_URL = "http://localhost:5000";
  const [socket, setSocket] = React.useState();

  React.useEffect(() => {
    const newSocket = io(SOCKET_SERVER_URL);
    setSocket(newSocket);

    // Handle disconnection
    newSocket.on("disconnect", () => {
      console.log("Disconnected from server");
    });

    newSocket.on("chat", (data) => {
      setPastMessages((prevMessages) => [data.response, ...prevMessages]);
    })

    newSocket.on("username", (data) => {
      setUsername(data.username)
    })

    // Clean up connection on component unmount
    return () => {
      newSocket.disconnect();
    };
  }, []);

  const sendMessage = () => {
    // update first time past messages
    setPastMessages([currentMessage, ...pastMessages])
    // clear input field
    setCurrentMessage("")

    socket.emit("chat", {
      user_input: currentMessage,
    })
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
        paddingBottom: '1vh',
        overflowY: 'scroll',
        flexDirection: 'column-reverse',
        display: 'flex',
        alignItems: 'center',
      })}>
        {pastMessages.map((message, index) => {
          return <Typography 
          
          sx={{
            textAlign: 'justify',
            color: 'text.secondary',
            width: { sm: '50%', md: '50%' },
            alignSelf: { sm: 'center', md: 'center' },
            justifySelf: { sm: 'center', md: 'center'},
            marginTop: { sm: '10px', md: '10px'},
            backgroundColor: (pastMessages.length - index) % 2 === 0 ? "lightblue" : "lightgreen",
            padding: "15px",
            borderRadius: "10px",
            animation: 'slide-in 0.5s ease-in-out',
            '@keyframes slide-in': {
              '0%': {
              transform: 'translateY(50%)',
              opacity: 0,
              },
              '100%': {
              transform: 'translateX(0)',
              opacity: 1,
              },
            },
            fontSize: '1rem',
            boxShadow: '0px 4px 6px rgba(0, 0, 0, 0.1)',
          }}
          
          key={pastMessages.length - index}>
            <Typography sx={{color: 'text.primary', fontSize: '1rem'}}>
             {(pastMessages.length - index) % 2 !== 0 ? "Assistant: " : (username || "Utilisateur") + ": " } 
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
        <ProductShowcase/>
        <Footer />
      </div>
    </AppTheme>
  );
}
