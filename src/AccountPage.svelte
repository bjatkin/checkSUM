<div class="parent head">
    <div class="center">
        <div class="mdc-typography--headline4 theme-primary-color">My Account</div>
        <div class="center name-container">
            <div class="half mdc-typography--body1 theme-secondary-color">{firstName}</div>
            <div class="half mdc-typography--body1 theme-secondary-color">{lastName}</div>
        </div>
    </div>

    <Verifyable label="Birth Date: {birthDate}" pCount="3"></Verifyable>

    <hr>

    <!--Verifyable label="Employment: Refer.io" pCount="1"></Verifyable-->
</div>

<script>
    import Verifyable from './Verifyable.svelte';

    export let firstName = "First_Name";
    export let lastName = "Last_Name";
    export let birthDate = "MM/DD/YYYY";

</script>

<style>
    .parent {
        text-align: center;
    }

    .center {
        margin: auto;
        max-width: 400px;
    }

    .head {
        margin: 40px 10px 20px;
    }

    .half {
        width: 50%;
        float: left;
    }

    .name-container {
        height: 40px;
        padding: 20px 0px;
    }
</style>