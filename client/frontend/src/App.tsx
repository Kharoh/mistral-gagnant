import React from 'react';
import MarketingPage from './marketing-page/MarketingPage'; 
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import InfoPage from "./marketing-page/infopage" ;

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<MarketingPage/>}></Route>
        <Route path="/vos_infos" element={<InfoPage/>}></Route>
      </Routes>
    </Router>
  );
};

export default App;