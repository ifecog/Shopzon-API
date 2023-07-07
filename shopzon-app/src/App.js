import {BrowserRouter as Router, Routes, Route} from 'react-router-dom'
import {Container} from 'react-bootstrap'

import HomeScreen from './screens/HomeScreen'

function App() {
  return (
    <Router>
      <main className='py-3'>
        <Container>
          <Routes>
            <Route path='/' element={<HomeScreen />} exact />
          </Routes>
        </Container>
      </main>
    </Router>
  )
}

export default App
