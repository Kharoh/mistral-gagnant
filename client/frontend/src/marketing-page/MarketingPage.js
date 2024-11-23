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

export default function MarketingPage(props) {

  const [currentMessage, setCurrentMessage] = React.useState("");
  const [pastMessages, setPastMessages] = React.useState([]);
  const [username, setUsername] = React.useState("");

  const sendMessage = () => {
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
      setPastMessages([...pastMessages, currentMessage, data.response])
    })
    .catch(error => console.error('Error:', error));
  }

  React.useEffect(() => console.log(pastMessages), [pastMessages])

  // listen for the response from the server to store the messages in pastMessages
  // React.useEffect(() => {
  //   const interval = setInterval(() => {
  //     fetch('http://localhost:5000/chat', {
  //       method: 'GET',
  //     })
  //     .then(response => response.json())
  //     .then(data => {
  //       setPastMessages(data)
  //     })
  //   }, 1000);
  //   return () => clearInterval(interval);
  // }, []);

  return (
    <AppTheme {...props}>
      <CssBaseline enableColorScheme />
      <AppAppBar />
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
