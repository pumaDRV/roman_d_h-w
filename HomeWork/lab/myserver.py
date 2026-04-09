from datetime import datetime, timedelta
from threading import Lock
from typing import Dict, List

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Unusual Clocks API")


class ClockView(BaseModel):
    id: int
    name: str
    kind: str
    initial_time: str
    current_time: str
    ticks_count: int


class BaseClock:
    def __init__(self, clock_id: int, name: str, kind: str, initial_time: str) -> None:
        self.id = clock_id
        self.name = name
        self.kind = kind
        self.initial_time = initial_time
        self._current_dt = datetime.strptime(initial_time, "%H:%M:%S")
        self.ticks_count = 0

    def _step_seconds(self) -> int:
        return 1

    def tick(self) -> None:
        self._current_dt += timedelta(seconds=self._step_seconds())
        self.ticks_count += 1

    def _time_str(self) -> str:
        return self._current_dt.strftime("%H:%M:%S")

    def as_dict(self) -> Dict[str, str | int]:
        return {
            "id": self.id,
            "name": self.name,
            "kind": self.kind,
            "initial_time": self.initial_time,
            "current_time": self._time_str(),
            "ticks_count": self.ticks_count,
        }


class NormalClock(BaseClock):
    pass


class ReverseClock(BaseClock):
    def _step_seconds(self) -> int:
        return -1


class InvisibleClock(BaseClock):
    FORBIDDEN_DIGITS = {"3", "7"}

    def tick(self) -> None:
        self._current_dt += timedelta(seconds=1)
        while self._has_forbidden_digits():
            self._current_dt += timedelta(seconds=1)
        self.ticks_count += 1

    def _has_forbidden_digits(self) -> bool:
        compact_time = self._current_dt.strftime("%H%M%S")
        return any(digit in compact_time for digit in self.FORBIDDEN_DIGITS)


clocks: Dict[int, BaseClock] = {
    1: NormalClock(1, "Обычные часы", "normal", "12:00:00"),
    2: ReverseClock(2, "Часы-наоборот", "reverse", "18:30:00"),
    3: InvisibleClock(3, "Часы-невидимки", "invisible", "22:59:58"),
}
clocks_lock = Lock()


def get_clock_or_404(clock_id: int) -> BaseClock:
    clock = clocks.get(clock_id)
    if clock is None:
        raise HTTPException(status_code=404, detail="Clock not found")
    return clock


@app.get("/clocks", response_model=List[ClockView])
def get_all_clocks() -> List[ClockView]:
    with clocks_lock:
        return [ClockView(**clock.as_dict()) for clock in clocks.values()]


@app.get("/clocks/{clock_id}", response_model=ClockView)
def get_clock(clock_id: int) -> ClockView:
    with clocks_lock:
        clock = get_clock_or_404(clock_id)
        return ClockView(**clock.as_dict())


@app.get("/clocks/{clock_id}/tick", response_model=ClockView)
@app.post("/clocks/{clock_id}/tick", response_model=ClockView)
def tick_clock(clock_id: int) -> ClockView:
    with clocks_lock:
        clock = get_clock_or_404(clock_id)
        clock.tick()
        return ClockView(**clock.as_dict())


if __name__ == "__main__":
    uvicorn.run("myserver:app", host="127.0.0.1", port=8000, reload=True)
