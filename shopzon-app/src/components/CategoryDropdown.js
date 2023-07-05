import React from 'react'
import {NavDropdown} from 'react-bootstrap'

const CategoryDropdown = ({categories}) => {
  const items = categories.map((category) => (
    <NavDropdown.Item
      key={category.id}
      text={category.name}
      href={`/products/${category.id}`}
    />
  ))

  return (
    <NavDropdown title='Categories' id='categories'>
      {items}
    </NavDropdown>
  )
}

export default CategoryDropdown
