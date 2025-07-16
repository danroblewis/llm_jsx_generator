<div className="card w-75 shadow-sm">
  <div className="card-body">
    <h5 className="card-title">User Profile</h5>
    <div className="row">
      <div className="col-md-6">
        <div className="mb-2">
          <span className="text-muted">Name:</span>
          <span className="text-break" style={{maxWidth: '200px', display: 'block', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap'}}>{props.name}</span>
        </div>
        <div className="mb-2">
          <span className="text-muted">City:</span>
          <span className="text-break" style={{maxWidth: '200px', display: 'block', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap'}}>{props.city}</span>
        </div>
      </div>
      <div className="col-md-6">
        <div className="mb-2">
          <span className="text-muted">Email:</span>
          <span className="text-break" style={{maxWidth: '200px', display: 'block', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap'}}>{props.contact && props.contact.email}</span>
        </div>
        <div className="mb-2">
          <span className="text-muted">Phone:</span>
          <span className="text-break" style={{maxWidth: '200 -px', display: 'block', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap'}}>{props.contact && props.contact.phone}</span>
        </div>
      </div>
    </div>
    <div className="mt-3">
      <h6 className="text-muted">Contact Details:</h6>
      <ul className="list-group list-group-flush">
        <li className="list-group-item">
          <span className="text-muted">Email:</span> {props.contact && props.contact.email}
        </li>
        <li className="list-group-item">
          <span className="text-muted">Phone:</span> {props.contact && props.contact.phone}
        </li>
      </ul>
    </div>
  </div>
</div>