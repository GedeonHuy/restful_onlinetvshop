import React from "react";
import PropTypes from "prop-types";
import key from "weak-key";
const ProductTable = ({ data }) =>
  !data.length ? (
    <p>Nothing to show</p>
  ) : (
    <div className="column">
      <h2 className="subtitle">
        Showing <strong>{data.length} products</strong>
      </h2>
      <table className="table is-striped">
        <thead>
          <tr>
            <th>id</th>
            <th>Title</th>
            <th>Price</th>
            <th>Brand</th>
            <th>Quantity</th>
          </tr>
        </thead>
        <tbody>
          {data.map((el, index) => (
            <tr key={index}>
              <td>{index+1}</td>
              <td>{(Object.values(el))[0]}</td>
              <td>${(Object.values(el))[1]}</td>
              <td>{(Object.values(el))[5]}</td>
              <td>{(Object.values(el))[2]}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
ProductTable.propTypes = {
  data: PropTypes.array.isRequired
};
export default ProductTable;