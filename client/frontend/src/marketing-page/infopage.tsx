import './infopage.css';
import * as React from 'react';
import CssBaseline from '@mui/material/CssBaseline';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import AppAppBar from './components/AppAppBar';
import Footer from './components/Footer';
import AppTheme from '../shared-theme/AppTheme';

export default function InfoPage(props) {
  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    alert('Formulaire envoyé!');
  };

  return (
    <AppTheme {...props}>
      <CssBaseline enableColorScheme />
      <Box display="flex" flexDirection="column" minHeight="100vh" width="99vw">
        <AppAppBar />
        <Box flexGrow={1} display="flex" alignItems="center" className="main-container">
          <Container maxWidth="md">
            <Box className="form-wrapper">
              <div className="form-container">
                <h1>Entrez vos informations</h1>
                <form onSubmit={handleSubmit}>
                  <div className="form-group">
                    <label htmlFor="company">
                      Nom de votre entreprise :
                    </label>
                    <input 
                      type="text" 
                      id="company"
                      name="company" 
                      required 
                    />
                  </div>
                  
                  <div className="form-group">
                    <label htmlFor="email">
                      Votre email :
                    </label>
                    <input 
                      type="email" 
                      id="email"
                      name="email" 
                      required 
                    />
                  </div>
                  
                  <div className="form-group">
                    <label htmlFor="phone">
                      Votre numéro :
                    </label>
                    <input 
                      type="text" 
                      id="phone"
                      name="phone" 
                      required 
                    />
                  </div>
                  
                  <div className="button-container">
                    <button type="submit">Envoyer</button>
                  </div>
                </form>
              </div>
            </Box>
          </Container>
        </Box>
        <Footer />
      </Box>
    </AppTheme>
  );
}