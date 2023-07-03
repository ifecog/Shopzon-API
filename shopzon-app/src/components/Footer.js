import React from 'react'
import {Row, Col, Container} from 'react-bootstrap'

function Footer() {
  const currentYear = new Date().getFullYear()

  return (
    <div>
      <footer>
        <Container>
          <Row>
            <Col className='text-center py-3'>
              Copyright @copy; {currentYear} Shopzon. All rights reserved.
            </Col>
          </Row>
        </Container>
      </footer>
    </div>
  )
}

export default Footer
