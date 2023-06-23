import React from 'react';
import './App.css';
import Nav from './admin/components/Nav';
import Menu from './admin/components/Menu'; 
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Stocks from './admin/Stocks';
import Main from './main/Main';


function App() {
  return (
    <Router>
      <div className="App">

                <Routes>main
                  <Route path='/' element={<Main />} />
                  <Route path='/admin/stocks' element={<Stocks />} />
                </Routes>

      </div>
    </Router>
  );
}

export default App;
