class ActivityLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    action = db.Column(db.String(120))
    details = db.Column(db.String(120))

    def __repr__(self):
        return '<ActivityLog {}>'.format(self.action)


User.activity_logs = db.relationship('ActivityLog', backref='user', lazy='dynamic')
