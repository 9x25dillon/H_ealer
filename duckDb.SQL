CREATE TABLE suites (
    id UUID PRIMARY KEY DEFAULT uuidv7(),
    name VARCHAR NOT NULL,
    version VARCHAR NOT NULL,
    description VARCHAR,
    metadata JSON,
    created_at TIMESTAMPTZ DEFAULT current_timestamp,
    UNIQUE(name, version)
);
