class Make(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    country: str
    founded: int


class Car(SQLModel, table=True):
    vin: int = Field(primary_key=True)
    year: int
    color: str
    mileage: int
    transmission: str


class ServiceRecord(SQLModel, table=True):
    date: str
    mileage: int
    description: str | None = None
    cost: int


class Tag(Enum):
    track = "track"
    daily = "daily"
    project = "project"
