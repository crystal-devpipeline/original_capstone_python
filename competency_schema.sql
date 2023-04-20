CREATE TABLE IF NOT EXISTS Users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT,
    email TEXT UNIQUE NOT NULL,
    phone TEXT,
    password TEXT NOT NULL,
    date_created TEXT,
    hire_date TEXT,
    user_type TEXT,
    active INTEGER DEFAULT 1
);

CREATE TABLE IF NOT EXISTS Competencies(
    competency_id INTEGER PRIMARY KEY,
    name TEXT,
    date_created INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS Assessments(
    assessment_id INTEGER PRIMARY KEY,
    competency_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    date_created TEXT NOT NULL,
    FOREIGN KEY(competency_id)
        REFERENCES Competencies(competency_id)
);

CREATE TABLE IF NOT EXISTS Assessment_results(
    assessment_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    score TEXT NOT NULL,
    date_taken TEXT NOT NULL,
    manager_id TEXT NOT NULL,
    competency_id TEXT NOT NULL,
    FOREIGN KEY(assessment_id)
        REFERENCES Assessments(assessment_id),
    FOREIGN KEY(user_id)
        REFERENCES Users(user_id),
    FOREIGN KEY(competency_id) 
        REFERENCES Assessments(competency_id)
);
