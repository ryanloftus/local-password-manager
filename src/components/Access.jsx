import React from 'react';

export const Access = () => {
    return (
        <div className="card ">
            <div class="card-body justify-center">
                <h2 class="card-title">Enter your passcode to view and edit passwords</h2>
                <input type="password" placeholder="Passcode" class="input input-bordered input-accent w-full max-w-xs" />
            </div>
        </div>
    );
};
