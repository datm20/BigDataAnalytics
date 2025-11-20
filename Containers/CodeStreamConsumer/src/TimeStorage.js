class TimeStorage {
    static #myInstance = null;
    static getInstance() {
        TimeStorage.#myInstance = TimeStorage.#myInstance || new TimeStorage();
        return TimeStorage.#myInstance;
    }

    #myTimes = [];

    get numberOfClones() { return this.#myTimes.length; }


    storeTime(file, timer) {
        let array = {name: file.name, total:timer.total, match:timer.match}
        console.log(array);
        this.#myTimes.push(array);
    }

    get clones() { return this.getTime(); }
    getAllTime() { return this.#myTimes; }
}

module.exports = TimeStorage;
