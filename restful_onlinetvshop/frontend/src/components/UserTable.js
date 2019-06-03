import React from "react";
import PropTypes from "prop-types";
import key from "weak-key";
const UserTable = ({ data }) =>
  !data.length ? (
    <p>Nothing to show</p>
  ) : (
    <div className="column">
      <h2 className="subtitle">
        Showing <strong>{data.length} items</strong>
      </h2>
      <table className="table is-striped">
        <thead>
          <tr>
            <th>id</th>
            <th>Username</th>
            <th>First</th>
            <th>Last</th>
            <th>Email</th>
          </tr>
        </thead>
        <tbody>
          {data.map((el, index) => (
            <tr key={index}>
              <td>{index+1}</td>
              <td>{(Object.values(el))[4]}</td>
              <td>{(Object.values(el))[5]}</td>
              <td>{(Object.values(el))[6]}</td>
              <td>{(Object.values(el))[7]}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
UserTable.propTypes = {
  data: PropTypes.array.isRequired
};
export default UserTable;